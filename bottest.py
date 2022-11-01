from telegram import Update, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters, ConversationHandler


def start(updater: Update, context:CallbackContext): # Hardoyim bulish sharit
    updater.message.reply_text(f"Assalomu Alaykum {updater.effective_user.full_name} \n  < IT /> O'quv markazimizga hush kelibsiz. Ismingiz va Familiyangizni kiriting: ✍️")
    #if updater.message.text != updater.message.text([[], "", []]):
        #updater.message.reply_text("ism va familiyani Xato kiritingiz.\n Misol: Sarvarbek Jakbarov")

    return 2
def malumot(updater: Update, context: CallbackContext):
    malumott = [[KeyboardButton("Markaz haqida ma'lumot")]]
    if updater.message.text=="Markaz haqida ma'lumot":
        updater.message.reply_text("Markaz nomi: IT academy \n 2019-yili Sarvarbek tomonidan asos solingan \n Kurslarimiz narxi har biri: 400000 so'mdan")
def fname(updater:Update, context:CallbackContext):
    fname_my = updater.message.text
    updater.message.reply_text("Yoshingizni kiriting  ✍️")


    return 3
def age(updater:Update, context:CallbackContext):
    go_to = [ # kinobka uchun uzgaruvchi
        [KeyboardButton("⬅️Oldinga")]
    ]

    updater.message.reply_text("Kengi bo'limga utilsinmi!", reply_markup=ReplyKeyboardMarkup(go_to, resize_keyboard=True))
    age_my = updater.message.text
    return 4
def menu(updater:Update, context:CallbackContext):
    info_button = [
        [KeyboardButton("🍴 Menyu")],
        [KeyboardButton("🛍 Mening buyurtmalarim")],
        [KeyboardButton("✍️ Fikr bildirish"), KeyboardButton("⚙️ Sozlamalar")],

    ]
    updater.message.reply_text("Quydagilardan birini tanlang..",
                               reply_markup=ReplyKeyboardMarkup(info_button, resize_keyboard=True))
    return 1
def post_message(updater:Update, context:CallbackContext):
    button_end = [
        [KeyboardButton("⬅️ Ortga")]
    ]
    msg = updater.message.text
    user = updater.message.from_user
    if msg == "⚙️ Sozlamalar":
        info_button = [
            [KeyboardButton("🖨 Malumot olish")],
            [KeyboardButton("✅ Malumot to'dirish")],
        ]
        updater.message.reply_text("Malumotlargiz! ",
                                   reply_markup=ReplyKeyboardMarkup(info_button, resize_keyboard=True))
        return 3
    elif msg == "✍️ Fikr bildirish":
        updater.message.reply_text("Yozing! ")

    elif msg == "🍴 Menyu":
        context.bot.send_photo(user.id, open("manzara.jpg.jpg",), caption=f"Code.xn ga xush kelibsiz\n{user.first_name}")
    else:
        updater.message.reply_text(f"{msg} bosildi", reply_markup=ReplyKeyboardMarkup(button_end, resize_keyboard=True))

    return 2
def main():
    TOKENT = "5140598303:AAE4pxD7ndjOFeWckffDjnV5mKQFHSABM8c"
    updater = Updater(TOKENT)
    all_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states = {
                1: [MessageHandler(Filters.text, post_message)],
                2: [MessageHandler(Filters.text, fname)],
                3: [MessageHandler(Filters.text, age)],
                4: [MessageHandler(Filters.text, menu)],
        },
        fallbacks=[]
    )
    updater.dispatcher.add_handler(all_handler)
    updater.start_polling()
    updater.idle()
if __name__ == "__main__":
    main()