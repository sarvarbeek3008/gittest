 # from telegram import Update
 # from telegram.ext import Updater,CommandHandler,CallbackContext,MessageHandler,Filters,ConversationHandler

#
# def start (updater:Update , context:CallbackContext):
#     updater.message.reply_text("Assalomu alaykum")
#
# def name(updater:Update , context:CallbackContext):
#     ism = updater
#
#
#
#
# def main():
#     TOKEN="5108710771:AAEN4mI1nLxESXcX2dXTuL2DP5e39CJ8PHc"
#
#     updater=Updater(TOKEN)
#
#     all_handler = ConversationHandler(
#         entry_points=[CommandHandler("start",start)],
#         states={
#
#         },
#         fallbacks=[]
#     )
#     updater.dispatcher.add_handler(all_handler)
#     updater.start_polling()
#     updater.idle()
#
# if __name__=="__main__":
#     main()
#
#
#
#










# from telegram import Update, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
# from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters, ConversationHandler
#
#
#
# def start(updater:Update, context: CallbackContext):
#     updater.message.reply_text("Assalomu alaykum\n\n Ism yozing ✍️ ")
#     info_button = [
#         [KeyboardButton("🍴 Menyu")],
#         [KeyboardButton("🛍 Mening buyurtmalarim"), KeyboardButton("📋 Ma'lumotlaringiz")],
#         [KeyboardButton("✍️ Fikr bildirish"), KeyboardButton("⚙️ Sozlamalar")]
#     ]
#     updater.message.reply_text("Quydagilardan birini tanlang..",
#                                reply_markup=ReplyKeyboardMarkup(info_button, resize_keyboard=True))
#
#     return 1
# def name(updater:Update, context: CallbackContext):
#     ism = updater.message.text
#     user = updater.message.from_user
#     with open(f"{user.id}.text", 'w') as f:
#         f.write(f"\nMijozni ismi: {ism}")
#     updater.message.reply_text("Familiyangizni yozing! ✍️ ")
#
#     return 2
# def surname(updater:Update, context: CallbackContext):
#     fam = updater.message.text
#     user = updater.message.from_user
#
#     with open(f"{user.id}.text", 'a') as f:
#         f.write(f"\nMijozni Familiyasi: {fam}")
#     updater.message.reply_text("Yoshiningizni yozing!")
#
#
#     return 3
# def age(updater:Update, context: CallbackContext):
#     yoshi = updater.message.text
#     user = updater.message.from_user
#
#     with open(f"{user.id}.text", 'a') as f:
#         f.write(f"\nMijozni Familiyasi: {yoshi}")
#     updater.message.reply_text("Otangizni ismini yozing!")
#
#     return 4
# def fathersname(updater:Update,context:CallbackContext):
#     fathername = updater.message.text
#     user = updater.message.from_user
#     with open(f"{user.id}.text",'a') as f:
#         f.write(f"\nMijozni otasini ismi:{fathername}")
#     #
#     # with open(f"{user.id}.text", "r") as f:
#     #     info = f.read()
#     #     updater.message.reply_text(f"ID:{user.id}\n\nKiritilgan ma'lumot tug'rimi!: {info}")
# #     return 5
# # def start1(updater:Update, context:CallbackContext):
# #     info_button = [
# #         [KeyboardButton("🍴 Menyu")],
# #         [KeyboardButton("🛍 Mening buyurtmalarim"), KeyboardButton("📋 Ma'lumotlaringiz")],
# #         [KeyboardButton("✍️ Fikr bildirish"), KeyboardButton("⚙️ Sozlamalar") ]
# #     ]
# #     updater.message.reply_text("Quydagilardan birini tanlang..", reply_markup=ReplyKeyboardMarkup(info_button, resize_keyboard=True))
# # INFO=("📋 Ma'lumotlaringiz")
#
#     return 5
# def post_message(updater:Update, context:CallbackContext):
#     msg = updater.message.text
#     updater.message.reply_text(f"{msg} O'tildi")
#
# #     return 6
# def information(updater,context):
#     user = updater.message.from_user
#     with open(f"{user.id}.text", "r") as f:
#         info = f.read()
#         updater.message.reply_text(f"ID:{user.id}\n\nKiritilgan ma'lumot tug'rimi!: {info}")
#
# def main():
#     # TOKENT = "5156094794:AAH1GzSb64Dh5vgHUwOs6_QJculehTkVDhs"
#     TOKEN='5108710771:AAEN4mI1nLxESXcX2dXTuL2DP5e39CJ8PHc'
#     updater = Updater(TOKEN)
#
#     all_handler = ConversationHandler(
#         entry_points=[CommandHandler("start", start)],
#         states = {
#             1 : [MessageHandler(Filters.text, name)],
#             2 : [MessageHandler(Filters.text, surname)],
#             3 : [MessageHandler(Filters.text, age)],
#             4 : [MessageHandler(Filters.text,fathersname)],
#             5 : [MessageHandler(Filters.text, post_message)],
#             # 6 : [MessageHandler(Filters.regex('^(' + INFO + ')$'), information)]
#         },
#         fallbacks = []
#     )
#     updater.dispatcher.add_handler(all_handler)
#     updater.start_polling()
#     updater.idle()
#
# if __name__=="__main__":
#     main()

#
# from telegram import Update, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
# from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters, ConversationHandler
#
#
# def start(updater:Update, context:CallbackContext):
#     updater.message.reply_text("Assalomu alaykum\n\n Ism yozing ✍️ ")
#     info_button = [
#         [KeyboardButton("🍴 Menyu")],
#         [KeyboardButton("🛍 Mening buyurtmalarim"), KeyboardButton("Ma'lumotlarim")],
#         [KeyboardButton("✍️ Fikr bildirish"), KeyboardButton("⚙️ Sozlamalar") ]
#     ]
#
#     updater.message.reply_text("Quyidagilardan birini tanlang..", reply_markup=ReplyKeyboardMarkup(info_button, resize_keyboard=True))
#     # updater.message.reply_text("Quyidagilardan birini tanlang..",
#     #                            reply_markup=ReplyKeyboardMarkup(info_button, resize_keyboard=True))
#     return 1
# def name(updater:Update, context: CallbackContext):
#     ism = updater.message.text
#     user = updater.message.from_user
#
#     with open(f"{user.id}.text", 'w') as f:
#         f.write(f"\nMijozni ismi: {ism}")
#     updater.message.reply_text("Familiyangizni yozing! ✍️ ")
#
#     return 2
# def surname(updater:Update, context: CallbackContext):
#     fam = updater.message.text
#     user = updater.message.from_user
#
#     with open(f"{user.id}.text", 'a') as f:
#         f.write(f"\nMijozni Familiyasi: {fam}")
#     updater.message.reply_text("Yoshiningizni yozing ✍!")
#     return 3
# def age(updater:Update, context: CallbackContext):
#     yoshi = updater.message.text
#     user = updater.message.from_user
#
#     with open(f"{user.id}.text", 'a') as f:
#         f.write(f"\nMijozni Yoshi: {yoshi}")
#     updater.message.reply_text("Otangizni ismini yozing ✍!")
#
#     return 4
# def fathersname(updater:Update,context:CallbackContext):
#     fathername = updater.message.text
#     user = updater.message.from_user
#     with open(f"{user.id}.text",'a') as f:
#         f.write(f"\nMijozni otasini ismi:{fathername}")
# #     return 5
# def information(updater, context):
#     user = updater.message.from_user
#     with open(f"{user.id}.text", "r") as f:
#         info = f.read()
#     updater.message.reply_text(f"ID:{user.id}\n\nKiritilgan ma'lumot tug'rimi!: {info}")

#     return 5
# def buttons(updater:Update,context:CallbackContext):
#     info_button = [
#         [KeyboardButton("🍴 Menyu")],
#         [KeyboardButton("🛍 Mening buyurtmalarim"), KeyboardButton("Ma'lumotlarim")],
#         [KeyboardButton("✍️ Fikr bildirish"), KeyboardButton("⚙️ Sozlamalar")]
#     ]
#
#     return 5
# def post_message(updater:Update, context:CallbackContext):
#     msg = updater.message.text
#     updater.message.reply_text(f"{msg} ga O'tildi")







#
# def main():
#     # TOKENT = "5156094794:AAH1GzSb64Dh5vgHUwOs6_QJculehTkVDhs"
#     TOKENT="5108710771:AAEN4mI1nLxESXcX2dXTuL2DP5e39CJ8PHc"
#     updater = Updater(TOKENT)
#
#
#     all_handler = ConversationHandler(
#         entry_points=[CommandHandler("start", start)],
#         states = {
#
#             1: [MessageHandler(Filters.text, name)],
#             2 : [MessageHandler(Filters.text, surname)],
#             3 : [MessageHandler(Filters.text, age)],
#             4 : [MessageHandler(Filters.text,fathersname)],
#             # 5 : [MessageHandler(Filters.text,information)],
#             # 5 : [MessageHandler(Filters.text, buttons)],
#             5: [MessageHandler(Filters.text, post_message)]
#         },
#         fallbacks=[]
#     )
#     updater.dispatcher.add_handler(all_handler)
#     updater.start_polling()
#     updater.idle()
#
# if __name__ == "__main__":
#     main()



















# PS C:\Users\User\PycharmProjects\Python> cd '.\My first  telegram bot\'
# PS C:\Users\User\PycharmProjects\Python\My first  telegram bot> ls
#
#
#     Каталог: C:\Users\User\PycharmProjects\Python\My first  telegram bot
#
#
# Mode                 LastWriteTime         Length Name
# ----                 -------------         ------ ----
# -a----        08.04.2022     16:56            887 BOT.py
# -a----        08.04.2022     16:57            613 BOT_1.py
#
#
# PS C:\Users\User\PycharmProjects\Python\My first  telegram bot> py .\BOT_1.py
# PS C:\Users\User\PycharmProjects\Python\My first  telegram bot> py .\BOT_1.py
# Exiting immediately!
# PS C:\Users\User\PycharmProjects\Python\My first  telegram bot>
#
#
# from telegram import Update, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
# from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters, ConversationHandler
#
#
# def start(updater: Update, context: CallbackContext):  # Hardoyim bulish sharit
#     updater.message.reply_text("Assalomu alakum \n\nIsm kirting: ✍️")  # BU botga malumotni pirosta ekranga chiqarish
#     # updater.message.text # Botga xabar junatsa qabul qiladi yani ushlob olish uchun
#     return 2
#
#
# def name(updater: Update, context: CallbackContext):
#     name_my = updater.message.text
#     updater.message.reply_text("Fam kiriting: ✍️")
#
#     return 3
#
#
# def fname(updater: Update, context: CallbackContext):
#     fname_my = updater.message.text
#     updater.message.reply_text("Yoshi kiriting  ✍️")
#
#     return 4
#
#
# def age(updater: Update, context: CallbackContext):
#     go_to = [  # kinobka uchun uzgaruvchi
#         [KeyboardButton("⬅️Oldinga")]
#         # KeyboardButton KInobka chiqarish () buni ichiga yozilgan malumot Knobkani ichiga yozlib qoladi
#     ]
#     # ReplyKeyboardMarkup -- BU kinobka uzgaruvchisini chaqirib beradi
#     # resize_keyboard = True -- Kinobka razmer ni kechkena qilib beradi
#     updater.message.reply_text("Kengi bo'limga utilsinmi!",
#                                reply_markup=ReplyKeyboardMarkup(go_to, resize_keyboard=True))
#     age_my = updater.message.text
#
#     return 5
#
#
# def menu(updater: Update, context: CallbackContext):
#     info_button = [
#         [KeyboardButton("🍴 Menyu")],
#         [KeyboardButton("🛍 Mening buyurtmalarim")],
#         [KeyboardButton("✍️ Fikr bildirish"), KeyboardButton("⚙️ Sozlamalar")]
#     ]
#     updater.message.reply_text("Quydagilardan birini tanlang..",
#                                reply_markup=ReplyKeyboardMarkup(info_button, resize_keyboard=True))
#
#     return 1
#
#
# def post_message(updater: Update, context: CallbackContext):
#     button_end = [
#         [KeyboardButton("⬅️ Ortga")]
#     ]
#     msg = updater.message.text
#     updater.message.reply_text(f"{msg} bosildi", reply_markup=ReplyKeyboardMarkup(button_end, resize_keyboard=True))
#
#     # return 2
#     # updater.message.reply_text(f"{msg} bo'limiga")
#
#
# def main():
#     # TOKENT = "5152426198:AAH6ksH_NarLcxzEcH7e5womTltYQccqEgk"
#     TOKENT = "5108710771:AAEN4mI1nLxESXcX2dXTuL2DP5e39CJ8PHc"
#
#     updater = Updater(TOKENT)
#
#     all_handler = ConversationHandler(
#         entry_points=[CommandHandler("start", start)],
#         states={
#             1: [MessageHandler(Filters.text, post_message)],
#             2: [MessageHandler(Filters.text, name)],
#             3: [MessageHandler(Filters.text, fname)],
#             4: [MessageHandler(Filters.text, age)],
#             5: [MessageHandler(Filters.text, menu)],  # bu def ni bajarish tartibi
#
#         },
#         fallbacks=[]
#     )
#     updater.dispatcher.add_handler(all_handler)
#     updater.start_polling()
#     updater.idle()
#
#
# if __name__ == "__main__":
#     main()
#
#
#
#
# from telegram import Update, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
# from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters, ConversationHandler
# #
#
# def start(updater:Update, context:CallbackContext): # Hardoyim bulish sharit
#     updater.message.reply_text("Assalomu alakum \n\nIsm kirting: ✍️") # BU botga malumotni pirosta ekranga chiqarish
#     # updater.message.text # Botga xabar junatsa qabul qiladi yani ushlob olish uchun
#     return 2
#
# def name(updater:Update, context:CallbackContext):
#     name_my = updater.message.text
#     updater.message.reply_text("Fam kiriting: ✍️")
#
#
#     return 3
# def fname(updater:Update, context:CallbackContext):
#     fname_my = updater.message.text
#     updater.message.reply_text("Yoshi kiriting  ✍️")
#
#
#     return 4
# def age(updater:Update, context:CallbackContext):
#     go_to = [ # kinobka uchun uzgaruvchi
#         [KeyboardButton("⬅️Oldinga")]  # KeyboardButton KInobka chiqarish () buni ichiga yozilgan malumot Knobkani ichiga yozlib qoladi
#     ]
#     # ReplyKeyboardMarkup -- BU kinobka uzgaruvchisini chaqirib beradi
#     # resize_keyboard = True -- Kinobka razmer ni kechkena qilib beradi
#     updater.message.reply_text("Kengi bo'limga utilsinmi!", reply_markup=ReplyKeyboardMarkup(go_to, resize_keyboard=True))
#     age_my = updater.message.text
#
#
#     return 5
# def menu(updater:Update, context:CallbackContext):
#     info_button = [
#         [KeyboardButton("🍴 Menyu")],
#         [KeyboardButton("🛍 Mening buyurtmalarim")],
#         [KeyboardButton("✍️ Fikr bildirish"), KeyboardButton("⚙️ Sozlamalar")],
#
#     ]
#     updater.message.reply_text("Quydagilardan birini tanlang..",
#                                reply_markup=ReplyKeyboardMarkup(info_button, resize_keyboard=True))
#
#     return 1
# def post_message(updater:Update, context:CallbackContext):
#     button_end = [
#         [KeyboardButton("⬅️ Ortga")]
#     ]
#     msg = updater.message.text
#     user = updater.message.from_user
#     if msg == "⚙️ Sozlamalar":
#         info_button = [
#             [KeyboardButton("🖨 Malumot olish")],
#             [KeyboardButton("✅ Malumot to'dirish")],
#         ]
#         updater.message.reply_text("Malumotlargiz! ",
#                                    reply_markup=ReplyKeyboardMarkup(info_button, resize_keyboard=True))
#         return 3
#     elif msg == "✍️ Fikr bildirish":
#         updater.message.reply_text("Yozing! ")
#
#     elif msg == "🍴 Menyu":
#         context.bot.send_photo(user.id, open("code.jpg", "rb"), caption=f"Code.xn ga xush kelibsiz\n{user.first_name}")
#     else:
#         updater.message.reply_text(f"{msg} bosildi", reply_markup=ReplyKeyboardMarkup(button_end, resize_keyboard=True))
#
#     return 2
#     # updater.message.reply_text(f"{msg} bo'limiga")
#
#
#
#
#
#
# def main():
#     TOKENT = "5152426198:AAH6ksH_NarLcxzEcH7e5womTltYQccqEgk"
#
#     updater = Updater(TOKENT)
#
#
#     all_handler = ConversationHandler(
#         entry_points=[CommandHandler("start", start)],
#         states = {
#                 1: [MessageHandler(Filters.text, post_message)],
#                 2: [MessageHandler(Filters.text, name)],
#                 3: [MessageHandler(Filters.text, fname)],
#                 4: [MessageHandler(Filters.text, age)],
#                 5: [MessageHandler(Filters.text, menu)], # bu def ni bajarish tartibi
#
#
#
#         },
#         fallbacks=[]
#     )
#     updater.dispatcher.add_handler(all_handler)
#     updater.start_polling()
#     updater.idle()
#
# if __name__  == "__main__":
#     main()


from telegram import Update, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters, ConversationHandler,CallbackQueryHandler
from valyuta import Valyuta

kurs = Valyuta()

val_dict = {
    "1":"USD",
    "2":"RUB",
    "3":"EUR"
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
    context.bot.send_photo(user.id, photo = open("804201997_8143.jpg", "rb"), caption="Assalomu alaykum biz sizga qanaqa yordam bera olamiz!", reply_markup=InlineKeyboardMarkup(valyuta_button))

    return 2
def converter(updater:Update,context:CallbackContext):
    query = updater .callback_query
    for i ,j in val_dict.items():
        if i == query.data and len(i)==1:
            info = kurs.getData(j)
            query.message.reply_text(f"1{j}=={info['Rate']}")
        elif i == query.data:
            j = j.split("_")
            info = kurs.getData(j[1])
            query.message.reply_text(f"1 UZS == {1 / float(info['Rate'])}")

def main():
    TOKENT="5108710771:AAEN4mI1nLxESXcX2dXTuL2DP5e39CJ8PHc"
    # TOKENT = "5248429602:AAGDNEtiHRBvk2L3lMW27jHHpfypWQ37TKo"

    updater = Updater(TOKENT)

    all_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            1: [MessageHandler(Filters.text, menu)],
            2 : [CallbackQueryHandler(converter)]
        },
        fallbacks=[]
    )

    updater.dispatcher.add_handler(all_handler)
    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()





























































