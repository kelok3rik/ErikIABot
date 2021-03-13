# mastrobot_example2.py

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

def start(update, context):
    update.message.reply_text('ErikMyers la pampara')

if __name__ == '__main__':
    updater = Updater(token='1583873873:AAFvY_UN8SHNq0ysoLPn6J6WSQp7CbbRqE0', use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start',start))

    updater.start_polling()
    updater.idle()