import yaml
from email_fetcher import EmailFetcher
from email_sender import EmailSender
from tg_bot import TgBot

# Load application.yaml
with open('application.yaml') as config_file:
    config = config_file.read()
app_config = yaml.load(config, Loader=yaml.FullLoader)

# Load application config keys
imap_server = app_config["credentials"]["imap"]["server"]
imap_username = app_config["credentials"]["imap"]["username"]
imap_password = app_config["credentials"]["imap"]["password"]
tg_token = app_config["credentials"]["telegram"]["token"]
email_folder_to_fetch = app_config["email-fetching"]["folder"]

# Initialize required components and variables
email_fetcher = EmailFetcher(imap_server, imap_username, imap_password)
last_fetch_uid = 0

#TODO: Change the third parameter to the email address you want to send the message to
email_sender = EmailSender(imap_username, imap_password, imap_username) 

# Create handler to send message
def send_message(update, context):
    message = update.message.text
    first_name = update.message.chat.first_name
    last_name = update.message.chat.last_name
    id =  update.message.chat.id
    email_sender.send(f'{first_name} {last_name} - {id}', message)


# Create handlers
def fetch_unread_messages(update, context):
    global last_fetch_uid
    msgs = email_fetcher.fetch_unread_emails(email_folder_to_fetch, (last_fetch_uid + 1))
    if (len(msgs)) == 0:
        update.message.reply_text('No unread messages.')
    else:
        for msg in msgs:
            msg_to_display = f'Subject: {msg.subject}\n From: {msg.from_}\n Message: {msg.text}'
            print(msg_to_display)
            update.message.reply_text(msg_to_display)
            last_fetch_uid = int(msg.uid)


# Create instance of bot components and start it
def main():
    bot = TgBot(tg_token, fetch_unread_messages, send_message)
    bot.send_message()


if __name__ == '__main__':
    main()