from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext,MessageHandler,Filters

def start(update: Update, context: CallbackContext):
    user = update . message.from_user
    print(update.message.from_user)
    # print(update.message.video)
    update.message.reply_text(f'Assalomu alaykum {user.first_name}')
    print(user.id)
def exo(update:Updater,context:CallbackContext):
    msg = update.message.text
    update.message.reply_text(msg)
    # if "Salom" ==msg:
    #     update.message.reply_text(msg)
updater = Updater('5108710771:AAEN4mI1nLxESXcX2dXTuL2DP5e39CJ8PHc')
updater.dispatcher.add_handler(CommandHandler('start',start))
updater.dispatcher.add_handler(MessageHandler(Filters.text,exo))
updater.start_polling()
updater.idle()












































