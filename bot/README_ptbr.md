# TelegramMonit V2

## Descrição

Este é um bot desenvolvido com Pyrogram para processar mensagens em um chat de origem e enviá-las para um chat de destino. O bot lida com vários tipos de mensagem, incluindo texto, fotos, documentos e vídeos. Em caso de restrição de encaminhamento, o bot baixa e reenvia as mídias.

## Estrutura do Projeto

- `bot/`
  - `config.py`: Configurações das credenciais e IDs dos chats.
  - `logging_config.py`: Configuração do logging.
  - `handler.py`: Funções para processar e enviar mensagens.
- `main.py`: Inicializa o cliente e configura o bot.
- `requirements.txt`: Dependências do projeto.

## Configuração

1. Clone o repositório:
   ```sh
   git clone https://github.com/andiimdevlp/TelegramMonitV2.git
   cd TelegramMonitV2

2. Instale as dependências:
    ```sh
    pip install -r requirements.txt

3. Configure suas credenciais e IDs no arquivo bot/config.py.

4. Execute o bot:
    ```sh
    python main.py


<a href="https://www.buymeacoffee.com/andiimdev" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-blue.png" alt="Buy Me A Coffee" style="height: 60px !important;width: 217px !important;" ></a>


# Licença
Este projeto está licenciado sob a MIT [License](https://choosealicense.com/licenses/mit/).
