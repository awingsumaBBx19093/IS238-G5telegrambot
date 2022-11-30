from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


class TgBot:
    def __init__(self, token, start_handler, message_handler):
        self.token = token
        self.start_handler = start_handler
        self.message_handler = message_handler

    def start(self):
        updater = Updater(self.token, use_context=True)
        dp = updater.dispatcher

        dp.add_handler(CommandHandler("start", self.start_handler))
        # dp.add_handler(MessageHandler(Filters.text, self.send_message))

        dp.add_error_handler(error)

        updater.start_polling()
        updater.idle()

    def send_message(self):
        updater = Updater(self.token, use_context=True)
        dp = updater.dispatcher

        dp.add_handler(CommandHandler("start", self.start_handler))
        dp.add_handler(MessageHandler(Filters.text, self.message_handler))

        dp.add_error_handler(error)

        updater.start_polling()
        updater.idle()


def error(update, context):
    print(f'Update {update} caused error {context.error}')