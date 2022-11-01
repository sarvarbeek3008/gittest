# from telegram import Update, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove, InlineKeyboardButton, InlineKeyboardMarkup
# from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters, ConversationHandler, CallbackQueryHandler
# from valyuta import Valyuta
#
# nimadir = Valyuta()
#
# valyu_dict = {
#     "1": "USD",
#     "2": "RUB",
#     "3": "EURO",
# }
#
# def start(updater: Update, context: CallbackContext):
#     button_info = [
#         [KeyboardButton("🇺🇿 O'zbek"), KeyboardButton("🇷🇺 Rus")]
#     ]
#     updater.message.reply_text("Assalomu alaykum Xush kelib siz",
#                                reply_markup=ReplyKeyboardMarkup(button_info, resize_keyboard=True))
#
#
#     return 1
#
# def menu(updater: Update, context: CallbackContext):
#     valyuta_button = [
#         [
#             InlineKeyboardButton('USD - UZS', callback_data="1"),
#             InlineKeyboardButton("RUB - UZS", callback_data="2"),
#             InlineKeyboardButton('EUR - UZS', callback_data="3")
#         ],
#         [
#             InlineKeyboardButton('UZS - USD', callback_data="1_1"),
#             InlineKeyboardButton("UZS - RUB", callback_data="2_2"),
#             InlineKeyboardButton("UZS - EUR", callback_data="3_3")
#         ]
#
#     ]
#     user = updater.message.from_user
#     context.bot.send_photo(user.id, photo = open("manzara.jpg.jpg", "rb"), caption="Assalomu alaykum biz sizga qanaqa yordam bera olamiz!", reply_markup=InlineKeyboardMarkup(valyuta_button))
#
#
# def converter(updater: Update, context: CallbackContext):
#     query = updater.callback_query
#     for i,j in valyu_dict.items():
#         if i == query.data:
#             info = nimadir.getData(j)
#             query.message.reply_text(f"1 {j} == {info['Rate']}")
#     return 2
# def main():
#     TOKENT = "5268987596:AAFtKDzD_YU-MMjOHi0j5VKcwto6_z0UeIM"
#
#     updater = Updater(TOKENT)
#
#     all_handler = ConversationHandler(
#         entry_points=[CommandHandler("start", start)],
#         states={
#             1: [MessageHandler(Filters.text, menu)],
#             2: [CallbackQueryHandler(converter)]
#         },
#         fallbacks=[]
#     )
#
#     updater.dispatcher.add_handler(all_handler)
#     updater.start_polling()
#     updater.idle()
#
#
# if __name__ == "__main__":
#     main()


from telegram import Update, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters, ConversationHandler


def start(updater:Update, context:CallbackContext): # Hardoyim bulish sharit
    updater.message.reply_text("Assalomu alakum \n\nIsm kirting: ✍️") # BU botga malumotni pirosta ekranga chiqarish
    # updater.message.text # Botga xabar junatsa qabul qiladi yani ushlob olish uchun
    return 2

def name(updater:Update, context:CallbackContext):
    name_my = updater.message.text
    updater.message.reply_text("Fam kiriting: ✍️")


    return 3
def fname(updater:Update, context:CallbackContext):
    fname_my = updater.message.text
    updater.message.reply_text("Yoshi kiriting  ✍️")


    return 4
def age(updater:Update, context:CallbackContext):
    go_to = [ # kinobka uchun uzgaruvchi
        [KeyboardButton("⬅️Oldinga")]  # KeyboardButton KInobka chiqarish () buni ichiga yozilgan malumot Knobkani ichiga yozlib qoladi
    ]
    # ReplyKeyboardMarkup -- BU kinobka uzgaruvchisini chaqirib beradi
    # resize_keyboard = True -- Kinobka razmer ni kechkena qilib beradi
    updater.message.reply_text("Kengi bo'limga utilsinmi!", reply_markup=ReplyKeyboardMarkup(go_to, resize_keyboard=True))
    age_my = updater.message.text


    return 5
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
        context.bot.send_photo(user.id, open("manzara.jpg.jpg", "rb"), caption=f"Code.xn ga xush kelibsiz\n{user.first_name}")
    else:
        updater.message.reply_text(f"{msg} bosildi", reply_markup=ReplyKeyboardMarkup(button_end, resize_keyboard=True))

    return 2
    # updater.message.reply_text(f"{msg} bo'limiga")






def main():
    TOKENT = "5278121475:AAGdmNeGAr3sfxSPvkL9OZIFf8bDLMMBrmk"

    updater = Updater(TOKENT)


    all_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states = {
                1: [MessageHandler(Filters.text, post_message)],
                2: [MessageHandler(Filters.text, name)],
                3: [MessageHandler(Filters.text, fname)],
                4: [MessageHandler(Filters.text, age)],
                5: [MessageHandler(Filters.text, menu)], # bu def ni bajarish tartibi



        },
        fallbacks=[]
    )
    updater.dispatcher.add_handler(all_handler)
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()