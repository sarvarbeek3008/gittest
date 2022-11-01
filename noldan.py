from telegram import Update, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove, InlineKeyboardButton,InlineKeyboardMarkup
from telegram.ext import Updater, CallbackContext, CommandHandler, ConversationHandler

tugma = [

        [InlineKeyboardButton("sarvarbek: ", callback_data="1")],
        [InlineKeyboardButton("azizchik", callback_data="2")]

]
tugma2 = [
    [KeyboardButton("jakbarov")],
    [KeyboardButton("sarvarbek")],
    [KeyboardButton("azizbek")],
    [KeyboardButton("abdurahmonov")],
    [KeyboardButton("alijon")],
    [KeyboardButton("abdunazarov")]
]

def start(update: Update, context: CallbackContext):
    update.message.reply_text("assalomualaykum botimizga hush kelibsiz: ",reply_markup=(InlineKeyboardMarkup(tugma, resize=True)))
    msg = update.message.text
    if msg == "jakbarov":
        update.message.reply_text("siz jakbarov tugmasini bosdingiz: ")
    elif msg == "alijon":
        update.message.reply_text("siz alijon tugmasini bosdingiz")
    return 1
def salom(update: Update, context: CallbackContext):
    update.message.reply_text("assalomu alaykum uz botimizga hush kelibsiz", reply_markup=(ReplyKeyboardMarkup(tugma2, resize_keyboard=True)))
    return 2
def qaytaruvchi(update: Update, context: CallbackContext):
    msg = update.message.text
    if msg == "jakbarov":
        update.message.reply_text("siz jakbarov tugmasini bosdingiz: ")
    elif msg == "alijon":
        update.message.reply_text("siz alijon tugmasini bosdingiz")
    return 3
updater = Updater('5322517077:AAHsQAZvGL65kqU_uBXbSQxOlWvj_ZFLtN0')
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('salom', salom))

updater.start_polling()
updater.idle()



from telegram import Update, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters, ConversationHandler


# def start(updater:Update, context:CallbackContext): # Hardoyim bulish sharit
#     updater.message.reply_text("Assalomu alakum \n\nIsmingizni kirting: ✍️") # BU botga malumotni pirosta ekranga chiqarish
#     # updater.message.text # Botga xabar junatsa qabul qiladi yani ushlob olish uchun
#     return 2
#
# def name(updater:Update, context:CallbackContext):
#     name_my = updater.message.text
#     updater.message.reply_text("Familiyangizni  kiriting: ✍ ")
#
#
#     return 3
# def fname(updater:Update, context:CallbackContext):
#     fname_my = updater.message.text
#     updater.message.reply_text("Yoshingizni kiriting  ✍️")
#
#
#     return 4
# def age(updater:Update, context:CallbackContext):
#     go_to = [ # kinobka uchun uzgaruvchi
#         [KeyboardButton("KEYINGI")]  # KeyboardButton KInobka chiqarish () buni ichiga yozilgan malumot Knobkani ichiga yozlib qoladi
#     ]
#     # ReplyKeyboardMarkup -- BU kinobka uzgaruvchisini chaqirib beradi
#     # resize_keyboard = True -- Kinobka razmer ni kechkena qilib beradi
#     updater.message.reply_text("Keyingi bo'limga utilsinmi!", reply_markup=ReplyKeyboardMarkup(go_to, resize_keyboard=True))
#     age_my = updater.message.text
#
#
#     return 5
# def menu(updater:Update, context:CallbackContext):
#     info_button = [
#         [KeyboardButton("cobalt")],
#         [KeyboardButton("nexia")],
#         [KeyboardButton("gentre"), KeyboardButton("spark")],
#
#     ]
#     updater.message.reply_text("Quydagilardan birini tanlang..",
#                                reply_markup=ReplyKeyboardMarkup(info_button, resize_keyboard=True))
#
#     return 1
# def post_message(updater:Update, context:CallbackContext):
#     button_end = [
#         [KeyboardButton("⬅️ bosh sahifaga")]
#     ]
#     msg = updater.message.text
#     user = updater.message.from_user
#     if msg == "cobalt":
#         info_button = [
#             [KeyboardButton("avtomat")],
#             [KeyboardButton("mexanika")],
#         ]
#         updater.message.reply_text("Malumotlargiz! ",
#                                    reply_markup=ReplyKeyboardMarkup(info_button, resize_keyboard=True))
#         return 3
#     elif msg == "avtomat":
#         updater.message.reply_text("Yozing! ")
#
#     elif msg == "mexanika":
#         context.bot.send_photo(user.id, photo=open("manzara.jpg.jpg", "rb"), caption=f"Code.xn ga xush kelibsiz\n{user.first_name}")
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
#     TOKENT = "5278121475:AAGdmNeGAr3sfxSPvkL9OZIFf8bDLMMBrmk"
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
# if __name__ == "__main__":
#     main()