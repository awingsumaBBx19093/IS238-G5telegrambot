from telegram.ext import *


class TgBot:
    def __init__(self, token, start_handler):
        self.token = token
        self.start_handler = start_handler

    def start(self):
        updater = Updater(self.token, use_context=True)
        dp = updater.dispatcher

        dp.add_handler(CommandHandler("start", self.start_handler))
        dp.add_error_handler(error)

        updater.start_polling()
        updater.idle()


def error(update, context):
    print(f'Update {update} caused error {context.error}')









