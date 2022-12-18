import threading
import sqlite3
import re

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


con = sqlite3.connect('chatbotDatabase.db', check_same_thread=False)
cur = con.cursor()


class TgBot:
    def __init__(self, config, email_fetcher, message_handler):
        self.config = config
        self.email_fetcher = email_fetcher
        self.message_handler = message_handler

    def start(self):
        updater = Updater(self.config.credentials_config.telegram_config.token, use_context=True)
        dp = updater.dispatcher

        dp.add_handler(CommandHandler("start", self._fetch_unread_emails_bg))
        dp.add_handler(MessageHandler(Filters.text, self.message_handler))
        dp.add_error_handler(error)

        updater.start_polling()
        updater.idle()

    
    def _fetch_unread_emails(self, update, context):
        self.email_fetcher.fetch_unread_emails(
                self.config.email_fetching_config.folder,
                lambda msg_to_display: self._display_message(update, msg_to_display)
            )

    def _fetch_unread_emails_bg(self, update, context):
        thread = threading.Thread(target=self._fetch_unread_emails, args=(update, context)) 
        thread.start()

    def _display_message(self, update, msg):
        h_m_id = str(msg.headers.get('message-id')) 
        h_m_id = re.sub('[(),\'\']', '', h_m_id )
        reply_to = (str(msg.headers.get('reply-to')))
        reply_to = re.sub('[(),\'\']', '', reply_to )

        cur.execute('''INSERT INTO tblMsgsLogs values (?, ?)''', (reply_to, h_m_id))
        con.commit()

        #if msg.size > 1000000, get only the first 1000000 bytes of the message
        if msg.size > 1000000:
            print('Message is too large for the bot to display. Please click on the link below to view the message.')
            print(f'https://mail.google.com/mail/u/0/#search/{msg.headers.get("message-id")}')
        #if msg.text is too long, get only the first 4096 bytes of the message
        if msg.text is None:
            print('Message body is empty. Please click on the link below to view the message.')
            print(f'https://mail.google.com/mail/u/0/#search/{msg.headers.get("message-id")}')
        elif len(msg.text) > 4096:
            print('Message body is too long for the bot to display. Please click on the link below to view the message.')
            print(f'https://mail.google.com/mail/u/0/#search/{msg.headers.get("message-id")}')


        # if message is too long, get only the first 1000 bytes of the message 
        if len(msg.text) > 4096:
            msg_to_display = f'From: {msg.from_}\nSubject: {msg.subject}\n\n{msg.text[:1000]}'
        else:

            msg_to_display = f'From: {msg.from_}\nSubject: {msg.subject}\n\n{msg.text}'
        print(msg_to_display)
        
        if update.message.reply_to_message: 
            update.message.reply_text(msg_to_display, reply_to_message_id=reply_to)
        else:
            update.message.reply_text(msg_to_display)
            
def error(update, context):
    print(f'Update {update} caused error {context.error}')