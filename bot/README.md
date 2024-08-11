# TelegramMonit V2

## Description

This is a bot developed with Pyrogram to process messages from a source chat and send them to a destination chat. The bot handles various types of messages, including text, photos, documents, and videos. In case of forwarding restrictions, the bot downloads and resends the media.

## Project Structure

- `bot/`
  - `config.py`: Configuration of credentials and chat IDs.
  - `logging_config.py`: Logging configuration.
  - `handler.py`: Functions to process and send messages.
- `main.py`: Initializes the client and sets up the bot.
- `requirements.txt`: Project dependencies.

## Setup

1. Clone the repository:
   ```sh
   git clone https://github.com/andiimdevlp/TelegramMonitV2.git
   cd TelegramMonitV2

2. Install the dependencies:
    ```sh
    pip install -r requirements.txt

3. Configure your credentials and IDs in the `bot/config.py` file.

4. Run the bot:
    ```sh
    python main.py


<a href="https://www.buymeacoffee.com/andiimdev" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-blue.png" alt="Buy Me A Coffee" style="height: 60px !important;width: 217px !important;" ></a>


# License

This project is licensed under the MIT [License](https://choosealicense.com/licenses/mit/).
