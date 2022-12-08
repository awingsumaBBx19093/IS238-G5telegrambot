from email_fetcher import EmailFetcher
from email_sender import EmailSender
from tg_bot import TgBot
from config import Config

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
    """
        subject = {id} This is to check wether update/sent message has content update_Id or rely_to_message.message_id, 
        then send message to sender and test message_id log via subject.
        This, can be changed to yaml subject config after testing.

        To test, send message to bot and check subject of sent message.
        Check the  'show original' of sent message and check the subject and message-ID.
        The current message subject is either the message_id or the reply_to_message.message_id.
    """
    
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
