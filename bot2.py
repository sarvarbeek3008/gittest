from telegram import Update, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters, ConversationHandler

info_button = [
    [KeyboardButton("NEXIA")],
    [KeyboardButton("COBALT")],
    [KeyboardButton("SPARK"), KeyboardButton("GENTRE")],

]
def start(updater: Update, context:CallbackContext): # Hardoyim bulish sharit
    updater.message.reply_text(f"Assalomu alakum. {updater.effective_user.full_name}. Siz namangandagi eng katta mashina bozori platfornasidasiz \n ------- \n Bo'limlardan birini tanlang ", reply_markup=ReplyKeyboardMarkup(info_button, resize_keyboard=True)) # BU botga malumotni pirosta ekranga chiqarish
    return 1
def mashina(updater: Update, context:CallbackContext):
    msg = updater.message.text
    user = updater.message.from_user
    if msg == "COBALT":
        info_button1 = [
            [KeyboardButton("AVTOMAT")],
            [KeyboardButton("MEXANIK")],
        ]
        updater.message.reply_text("Quydagilardan birini tanlang..",
                                   reply_markup=ReplyKeyboardMarkup(info_button1, resize_keyboard=True))
        if msg == "AVTOMAT":
            updater.message.reply_photo("https://i.trse.ru/2021/08/XH7A-1200x801.jpeg")
        elif msg == "MEXANIK":
            updater.message.reply_photo("https://i.trse.ru/2021/08/XH7A-1200x801.jpeg")

    elif msg == "SPARK":
        updater.message.reply_photo("https://i.trse.ru/2021/08/XH7A-1200x801.jpeg")

    elif msg == "NEXIA":
        tanlov_button = [
            [KeyboardButton("NEXIA1")],
            [KeyboardButton("NEXIA2")],
            [KeyboardButton("NEXIA3")],
            [KeyboardButton("ORTGA")],
        ]
        updater.message.reply_text("Quydagilardan birini tanlang..",
                                 reply_markup=ReplyKeyboardMarkup(tanlov_button, resize_keyboard=True))
        message1 = updater.message.text
        if message1 == "NEXIA1":
            updater.message.reply_photo("https://i.trse.ru/2021/08/XH7A-1200x801.jpeg")
        elif message1 == "NEXIA2":
            updater.message.reply_photo("https://i.trse.ru/2021/08/XH7A-1200x801.jpeg")
        elif msg == "NEXIA3":
            context.bot.send_photo(open("manzara.jpg.jpg","rb"))
        elif message1 == "ORTGA":
            button_end = [
                [KeyboardButton("ORTGA")]
            ]
            updater.message.reply_text(reply_markup=ReplyKeyboardMarkup(info_button, resize_keyboard = True))
        else:
            updater.message.reply_text("iltimos tugmalardan birini bosing")
    # elif msg == "GENTRE":
    #     context.bot.send_photo(open(""))

def main():
    TOKENT = "5268987596:AAFtKDzD_YU-MMjOHi0j5VKcwto6_z0UeIM"

    updater = Updater(TOKENT)

    all_handler = ConversationHandler(
        entry_points=[CommandHandler("start",start)],
        states={
            1: [MessageHandler(Filters.text, mashina)],
        },
        fallbacks=[]
    )
    updater.dispatcher.add_handler(all_handler)
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()