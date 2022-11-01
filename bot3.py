from telegram import Update, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove, InlineKeyboardButton, \
    InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters, ConversationHandler, \
    CallbackQueryHandler



def start(updete: Update, context: CallbackContext):
    updete.message.reply_text("Assalomu aleykum \n\n Ismi kiriteng! ")
    return 1
def name(updater: Update, context: CallbackContext):
    updater.message.reply_text("familliya kiriting")
    ism = updater.message.from_user
    return 2
def surname(updater: Update, context: CallbackContext):
    info_button = [
        [KeyboardButton("➡️Oldinga"), KeyboardButton("️⬅️Ortga")]
    ]
    # updater.message.reply_text("familliya yozing")
    familliya = updater.message.from_user
    updater.message.reply_text("Endi nima qilasiz", reply_markup=ReplyKeyboardMarkup(info_button))

    return 3
def Texnik(updater: Update, context: CallbackContext):
    button_menu = [
        [KeyboardButton("Texnikalar 🛠")],
        [KeyboardButton("Kiyimlar 👔"), KeyboardButton("Mashinalar 🚘"),]

    ]
    updater.message.reply_text("Quyidagilarni birini tanlang!!!", reply_markup=ReplyKeyboardMarkup(button_menu, resize_keyboard=True))


def main():
    TOKENT = "5332445019:AAFGmAtS9UKQXHtkaLKN6gQ5b70erBAI268"

    updater = Updater(TOKENT)

    all_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states = {
            1: [MessageHandler(Filters.text, name)],
            2: [MessageHandler(Filters.text, surname)],
            3: [MessageHandler(Filters.text, Texnik)]


        },
        fallbacks=[]
    )

    updater.dispatcher.add_handler(all_handler)
    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()