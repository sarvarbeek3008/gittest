from telegram import Update, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters, ConversationHandler, CallbackQueryHandler
from valyuta import Valyuta

nimadir = Valyuta()
# print(kurs)

val_dict = {
    "1": "USD",
    "2": "RUB",
    "3": "EUR",
    '1_1': 'UZS_USD',
    '2_2': "UZS_RUB",
    "3_3": "UZS_EUR",

}


def start(updater: Update, context: CallbackContext):
    button_info = [
        [KeyboardButton("🇺🇿 O'zbek"), KeyboardButton("🇷🇺 Rus")]
    ]
    updater.message.reply_text("Assalomu alaykum Xush kelib siz",
                               reply_markup=ReplyKeyboardMarkup(button_info, resize_keyboard=True))


    return 1

def menu(updater: Update, context: CallbackContext):
    valyuta_button = [
        [
            InlineKeyboardButton('USD - UZS', callback_data="1"),
            InlineKeyboardButton("RUB - UZS", callback_data="2"),
            InlineKeyboardButton('EUR - UZS', callback_data="3")
        ],
        [
            InlineKeyboardButton('UZS - USD', callback_data="1_1"),
            InlineKeyboardButton("UZS - RUB", callback_data="2_2"),
            InlineKeyboardButton("UZS - EUR", callback_data="3_3")
        ]

    ]
    user = updater.message.from_user
    context.bot.send_photo(user.id, photo = open("code.jpg", "rb"), caption="Assalomu alaykum biz sizga qanaqa yordam bera olamiz!", reply_markup=InlineKeyboardMarkup(valyuta_button))

    return 2
def converter(updater: Update, context: CallbackContext):
    query = updater.callback_query
    for i,j in val_dict.items():
        if  i == query.data and len(i) == 1:
            info = nimadir.getData(j)
            # print(info)
            query.message.reply_text(f"1 {j} == {info['Rate']}")
        elif i == query.data:
            j = j.split("_")
            info = nimadir.getData(j[1])
            query.message.reply_text(f"1 UZS == {1 / float(info['Rate'])}")


def main():
    TOKENT = "5278121475:AAGdmNeGAr3sfxSPvkL9OZIFf8bDLMMBrmk"

    updater = Updater(TOKENT)

    all_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            1: [MessageHandler(Filters.text, menu)],
            2: [CallbackQueryHandler(converter)]
        },
        fallbacks=[]
    )

    updater.start_polling()
    updater.idle()

    updater.dispatcher.add_handler(all_handler)

if __name__ == "__main__":
    main()