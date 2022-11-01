# from tokenize import Token
# from telegram import Update
# from telegram.ext import Updater,CommandHandler,CallbackContext,MessageHandler,Filters,ConversationHandler

# def start(updater: Updater, context: CallbackContext):
#     updater.message.reply_text(f"Assalomu alaykum: ")

#     TOKENT=''
#     updater=Updater(TOKENT)
# all_handler=ConversationHandler(
#     entry_points=[CommandHandler('start',start)]
#     states={

#     }
#     fallbacks=[]
# )

# updater.dispatcher.add_handler(all_handler)
# updater.start_polling()
# updater.idle()

# if __name__=="__main__":
#     main()

from bdb import effective
from telegram import Sticker, Update
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters, ConversationHandler


# def start(updater:Update, context:CallbackContext):
#     info_button = [
#         [KeyboardButton("🍴 Menyu")],
#         [KeyboardButton("🛍 Mening buyurtmalarim")],
#         [KeyboardButton("✍️ Fikr bildirish"), KeyboardButton("⚙️ Sozlamalar") ]
#     ]
#     updater.message.reply_text("Quydagilardan birini tanlang..", reply_markup=ReplyKeyboardMarkup(info_button, resize_keyboard=True))

#     return 1

def start(updater2: Update, context: CallbackContext):
    #msg2 = updater2.message.text 
    updater2.message.reply_text(f"Assalomu alaykum {updater2.effective_user.full_name}. Iltimos to'liq Ismingizni kiriting:  ")
    # if updater2.message.text == updater2.message.text():
    #     updater2.message.reply_text(f"Iltimos harflarda ismingizni kiriting: ")
    # else:
    #     updater2.message.reply_text(f"✔️")
    return 1

def post_message(updater:Update, context:CallbackContext):
    msg = updater.message.text
    updater.message.reply_text(f"Familiyangizni kiriting: ")
    return 2
    # updater.message.reply_text(f"{msg} bo'limiga")
def main():
    TOKENT = "5211616689:AAH1UZDJT_qUrzHP-PutiXZOZ49fz_-Opf4"

    updater = Updater(TOKENT)


    all_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states = {
                1: [MessageHandler(Filters.text, post_message)]
        },
        fallbacks=[]
    )
    updater.dispatcher.add_handler(all_handler)
    updater.start_polling()
    updater.idle()

if __name__=="__main__":
    main()