import telegram.ext

with open("token.txt", 'r') as f:
    token = f.read()
    
updater = telegram.ext.Updater(token)

def start(update,context):
    update.message.reply_text("Hi Welcome to CryptoLand")
    
dp = updater.dispatcher
dp.add_handler(telegram.ext.CommandHandler("start", start))

updater.start_polling()
updater.idle()

