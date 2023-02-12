import telegram.ext

with open("token.txt", 'r') as f:
    token = f.read()
    
updater = telegram.ext.Updater(token)

def start(update,context):
    update.message.reply_text("Hi Welcome to CryptoLand")
    
def Price(update,context):
    update.message.reply_text("Price Bitcoin : 200000$")    
    
dp = updater.dispatcher
dp.add_handler(telegram.ext.CommandHandler("start", start))
dp.add_handler(telegram.ext.CommandHandler("price", Price))

updater.start_polling()
updater.idle()

