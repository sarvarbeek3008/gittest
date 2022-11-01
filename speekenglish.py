from telegram import Update, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters, ConversationHandler


def start(updater: Update, context: CallbackContext):  # Hardoyim bulish sharit
    updater.message.reply_text("Assalomu alakum \n\nIsm kirting: ✍️")  # BU botga malumotni pirosta ekranga chiqarish
    # updater.message.text # Botga xabar junatsa qabul qiladi yani ushlob olish uchun
    return 2


def name(updater: Update, context: CallbackContext):
    name_my = updater.message.text
    updater.message.reply_text("Fam kiriting: ✍️")

    return 3


def fname(updater: Update, context: CallbackContext):
    fname_my = updater.message.text
    updater.message.reply_text("Yoshi kiriting  ✍️")

    return 4

def malumot(updater: Update, context: CallbackContext):
    updater.message.reply_text(f"Sizning malumotlaringiz quyidagilar: {updater.message.text}")
def age(updater: Update, context: CallbackContext):
     go_to = [  # kinobka uchun uzgaruvchi
         [KeyboardButton("⬅️Oldinga")]
         # KeyboardButton KInobka chiqarish () buni ichiga yozilgan malumot Knobkani ichiga yozlib qoladi
     ]
     # ReplyKeyboardMarkup -- BU kinobka uzgaruvchisini chaqirib beradi
     # resize_keyboard = True -- Kinobka razmer ni kechkena qilib beradi
     updater.message.reply_text("Kengi bo'limga utilsinmi!",
                                reply_markup=ReplyKeyboardMarkup(go_to, resize_keyboard=True))
     age_my = updater.message.text

     return 5


def menu(updater: Update, context: CallbackContext):
     info_button = [
         [KeyboardButton("🍴 Menyu")],
         [KeyboardButton("🛍 Mening buyurtmalarim")],
         [KeyboardButton("✍️ Fikr bildirish"), KeyboardButton("Sozlamalar")], KeyboardButton("Malumotlaringiz")
     ]
     updater.message.reply_text("Quydagilardan birini tanlang..",
                                reply_markup=ReplyKeyboardMarkup(info_button, resize_keyboard=True))

     return 1


def post_message(updater: Update, context: CallbackContext):
     button_end = [
         [KeyboardButton("⬅️ Ortga")]
     ]
     msg = updater.message.text
     updater.message.reply_text(f"{msg} bosildi", reply_markup=ReplyKeyboardMarkup(button_end, resize_keyboard=True))

     return 2
     updater.message.reply_text(f"{msg} bo'limiga")

def malumot(updater: Update, context: CallbackContext):
    if updater.message.text=='Sozlamalar':
        updater.message.reply_text(updater.message.text)
def main():
    TOKENT = "5278121475:AAGdmNeGAr3sfxSPvkL9OZIFf8bDLMMBrmk"

    updater = Updater(TOKENT)

    all_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            1: [MessageHandler(Filters.text, post_message)],
            2: [MessageHandler(Filters.text, name)],
            3: [MessageHandler(Filters.text, fname)],
            4: [MessageHandler(Filters.text, age)],
            5: [MessageHandler(Filters.text, menu)],  # bu def ni bajarish tartibi

        },
        fallbacks=[]
    )
    updater.dispatcher.add_handler(all_handler)
    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()