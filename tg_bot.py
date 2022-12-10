import threading

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


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
        #  TODO: Database to store message id and subject
        # This area here is for testing purposes
        
        msg_to_display = f'Subject: {msg.subject}\n From: {msg.from_}\n Message: {msg.text}'
        
        if update.message.reply_to_message:
            update.message.reply_text(msg_to_display, reply_to_message_id=msg.subject)

        else:
            update.message.reply_text(msg_to_display, reply_to_message_id=msg.subject)

def error(update, context):
    print(f'Update {update} caused error {context.error}')