import logging 
from pyrogram import Client, filters
import os
import json
from bot.config import SOURCE_CHAT_ID, TARGET_CHAT_ID

def log_message(log_entry, log_file='telegram_monit_log.json'):
    if not os.path.exists(log_file):
        with open(log_file, 'w') as f:
            json.dump([], f)  # Inicia o arquivo JSON com uma lista vazia

    with open(log_file, 'r+') as f:
        logs = json.load(f)
        logs.append(log_entry)
        f.seek(0)
        json.dump(logs, f, indent=4)

async def process_message(client, message):
    log_entry = {
        "id": message.message_id if hasattr(message, 'message_id') else message.id,
        "status": "sucesso",
        "legenda": message.text if message.text else "",
        "data": message.date.isoformat(),
        "remetente": message.chat.id,
        "tipo": "",
        "media": None
    }

    try:
        # Define o tipo de mensagem e coleta informações sobre a mídia
        if message.photo:
            log_entry["tipo"] = "foto"
            log_entry["media"] = {
                "document_id": message.photo.file_id,
                "size": message.photo.file_size if message.photo.file_size else None,
                "mime_type": "image/jpeg"
            }
        elif message.document:
            log_entry["tipo"] = "documento"
            log_entry["media"] = {
                "document_id": message.document.file_id,
                "size": message.document.file_size if message.document.file_size else None,
                "mime_type": message.document.mime_type if message.document.mime_type else "application/octet-stream"
            }
        elif message.video:
            log_entry["tipo"] = "video"
            log_entry["media"] = {
                "document_id": message.video.file_id,
                "size": message.video.file_size if message.video.file_size else None,
                "mime_type": message.video.mime_type if message.video.mime_type else "video/mp4"
            }
        else:
            log_entry["tipo"] = "texto"

        # Tenta enviar a mensagem diretamente para o chat de destino
        try:
            if message.media:
                file_path = await message.download()
                if file_path:
                    if log_entry["tipo"] == "foto":
                        await client.send_photo(TARGET_CHAT_ID, file_path, caption=message.caption)
                    elif log_entry["tipo"] == "documento":
                        await client.send_document(TARGET_CHAT_ID, file_path, caption=message.caption)
                    elif log_entry["tipo"] == "video":
                        await client.send_video(TARGET_CHAT_ID, file_path, caption=message.caption)
                    os.remove(file_path)
                    logging.info(f"Mídia baixada e enviada para {TARGET_CHAT_ID}")
            else:
                await client.send_message(TARGET_CHAT_ID, message.text)
                logging.info(f"Mensagem {log_entry['id']} enviada com sucesso para {TARGET_CHAT_ID}")
        except Exception as e:
            logging.error(f"Erro ao enviar mensagem diretamente: {e}")
            log_entry["status"] = "falha"
    except Exception as e:
        log_entry["status"] = "erro"
        logging.error(f"Erro ao processar mensagem: {e}")
    
    # Log da mensagem processada
    log_message(log_entry)
