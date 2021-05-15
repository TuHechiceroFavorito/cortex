from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging

import os

token = os.environ.get("cortex_tg")

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

def test(update, context):
    logging.info('Request for testing sent')
    context.bot.send_message(chat_id=update.effective_chat.id, text="Dani chupapollas")

def on(update, context):
    logging.info('Message to turn on the LED sent')
    context.bot.send_message(chat_id=update.effective_chat.id, text="Turning LED on")
    context.bot.send_message(chat_id=update.effective_chat.id, text="LED on")

def off(update, context):
    logging.info('Message to turn off the LED sent')
    context.bot.send_message(chat_id=update.effective_chat.id, text="Turning LED off")
    context.bot.send_message(chat_id=update.effective_chat.id, text="LED off")

def main():
    updater = Updater(token='1803680816:AAGOW6rlZk7LgUeODKDCF9sYPh5Wvr9kS9w', use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler('test', test))
    dp.add_handler(CommandHandler('on', on))
    dp.add_handler(CommandHandler('off', off))


    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()