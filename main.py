from email_fetcher import EmailFetcher
from email_sender import EmailSender
from tg_bot import TgBot
from config import Config

config = Config.load()

# Initialize required components and variables
email_fetcher = EmailFetcher(config.credentials_config.imap_config)
email_sender = EmailSender(config.credentials_config.imap_config)


# Create handler to send message
def send_message(update, context):
    message = update.message.text
    first_name = update.message.chat.first_name
    last_name = update.message.chat.last_name
    id = update.message.chat.id
    # TODO: Change the third parameter to the email address you want to send the message to
    email_sender.send(f'{first_name} {last_name} - {id}', message, config.credentials_config.imap_config.username)


# Create instance of bot components and start it
def main():
    tg_bot = TgBot(config, email_fetcher, send_message)
    tg_bot.start()


if __name__ == '__main__':
    main()
