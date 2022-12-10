from email_fetcher import EmailFetcher
from email_sender import EmailSender
from tg_bot import TgBot
from config import Config
import threading

config = Config.load()

# Initialize required components and variables
email_fetcher = EmailFetcher(config.credentials_config.imap_config)
email_sender = EmailSender(config.credentials_config.imap_config)
subject = config.send_email_config.subject

# Create handler to send message
def send_message(update, context):
    message = update.message.text
    print(update)


    id = update.message.message_id
    
    if update.message.reply_to_message:
        id = update.message.reply_to_message.message_id
        email_sender.send(f'{id}', message, config.credentials_config.imap_config.username)
    else:
        email_sender.send(f'{id}', message, config.credentials_config.imap_config.username)

# Create instance of bot components and start it
def main():
    tg_bot = TgBot(config, email_fetcher, send_message)
    tg_bot.start()

if __name__ == '__main__':
    main()
