from bdb import effective
from turtle import update
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext,MessageHandler,Filters, ConversationHandler



def start(update: Updater, context: CallbackContext):
    update.message.reply_text(f"Assalomu alykum ")
def main():
    TOKENT = '5211616689:AAH1UZDJT_qUrzHP-PutiXZOZ49fz_-Opf4'
    updater = Updater(TOKENT)

    all_handler = ConversationHandler (
        entry_points=[CommandHandler('start',start)],
        states = {


        },
        fallbacks=[]
    )
    updater.dispatcher.add_handler(all_handler)
    updater.start_polling()
    updater.idle()
if __name__=="__main__":
    main()

