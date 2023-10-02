import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text='Hi Welcome to CryptoLand')


def Price(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text='Price Bitcoin : 200000$')

def error(bot, update):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', bot, update.error)


def main():
    """Start the bot."""
    Token = '1226131623:uQiJSmRG7mwRsvj7Fc8iUWyuOkOy7eQ4qHC73KKl'
    updater = Updater(token=Token, base_url="https://tapi.bale.ai/bot")

    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("price", Price))

    dp.add_error_handler(error)
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()

