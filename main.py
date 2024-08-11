from pyrogram import Client, filters
from bot.config import API_ID, API_HASH, PHONE_NUMBER, SOURCE_CHAT_ID
from bot.logging_config import setup_logging
from bot.handler import process_message

def main():
    setup_logging()
    app = Client("telegram_monitv2", api_id=API_ID, api_hash=API_HASH, phone_number=PHONE_NUMBER)

    @app.on_message(filters.chat(SOURCE_CHAT_ID))
    async def my_handler(client, message):
        await process_message(client, message)

    app.run()

if __name__ == '__main__':
    main()
