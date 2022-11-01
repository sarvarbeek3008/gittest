from cgitb import text
from logging import Filter
from telegram import Update, KeyboardButton, InlineKeyboardButton, ReplyKeyboardMarkup,InlineKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import Updater, CommandHandler, CallbackContext, ConversationHandler, MessageHandler, Filters

tugma = [
    [KeyboardButton("menyu")],
    [KeyboardButton("buyurtmalarim")],
    [KeyboardButton("fikr bildirish")],
    [KeyboardButton("sozlamalar")]
]

tugma2 = [
    [KeyboardButton("fast food")],
    [KeyboardButton("ichimliklar")],
    [KeyboardButton("NEW:// O'zbek milliy taomlari")]
]
tugmasoz = [
    [KeyboardButton("malumotlaringiz")],
    [KeyboardButton("ortga")]
]

tugmain = [
    [InlineKeyboardButton("2345 ygug lavash",callback_data="1"),InlineKeyboardButton("hotdog",callback_data="2")],
    [InlineKeyboardButton("burger",callback_data="3"),InlineKeyboardButton("kartoshka free",callback_data="4")],
    [InlineKeyboardButton("twister",callback_data="5"),InlineKeyboardButton("chikken",callback_data="6")],
]
tugmain2 = [
    [InlineKeyboardButton("pepsi",callback_data="1"),InlineKeyboardButton("cola",callback_data="2")],
    [InlineKeyboardButton("fanta",callback_data="3"),InlineKeyboardButton("flesh",callback_data="4")],
    [InlineKeyboardButton("cofee",callback_data="5"),InlineKeyboardButton("choy",callback_data="6")]
]
tugmain3 = [
    [InlineKeyboardButton("osh",callback_data="1"),InlineKeyboardButton("lag'mon",callback_data="2")],
    [InlineKeyboardButton("mastava",callback_data="3"),InlineKeyboardButton("sho'rva",callback_data="4")]
]
def start(updater: Update, context: CallbackContext):
    updater.message.reply_text("assalomu alaykum botimizga hush kelibsiz.\n iltimos ismingizni kiriting: ")
    return 1
def familiya(updater: Update, context: CallbackContext):
    updater.message.reply_text("familiyangizni kiriting: ")
    return 2
def tugma1(updater: Update, context: CallbackContext):
    updater.message.reply_text("bolimlardan birini tanlang: ",reply_markup=ReplyKeyboardMarkup(tugma,resize_keyboard=True))
    return 3
def agar(updater: Update, context:CallbackContext):
    xabar=updater.message.text
    if xabar=="menyu":
        updater.message.reply_text("menyudagi narsalardan tanlang: ", reply_markup=ReplyKeyboardMarkup(tugma2,resize_keyboard=True))
    elif xabar=="buyurtmalarim":
        updater.message.reply_text("siz hali hech narsa buyurtma qilmadingiz")
    elif xabar=="fikr bildirish":
        updater.message.reply_text(f"fikrlaringizni @djakbarov ga yozishingiz mumkin ")
    elif xabar=="sozlamalar":
        updater.message.reply_text("malumotlaringizni bilmoqchimisiz",reply_markup=ReplyKeyboardMarkup(tugmasoz,resize_keyboard=True))
    return 4
def agar2(updater: Update, context: CallbackContext):
    msg = updater.message.text
    user = updater.message.chat_id
    if msg=="fast food":
        updater.message.reply_photo(photo=open("manzara.jpg.jpg","rb"),caption="tugmalardan birini tanlang",reply_markup=InlineKeyboardMarkup(tugmain))
        
        #updater.message.reply_text("ichimliklardan birini tanlang", reply_markup=InlineKeyboardMarkup(tugmain))  
        #context.bot.send_photo(user, photo=open("manzara.jpg.jpg","rb"),caption="yetkazib berish xizmati faqat vodiy boylab xolos",reply_markup=InlineKeyboardMarkup(tugmain)
    if msg=="ichimliklar":
        updater.message.reply_text("ichimliklardan birini tanlang", reply_markup=InlineKeyboardMarkup(tugmain2))
    if msg=="NEW:// O'zbek milliy taomlari":
        updater.message.reply_text("quyidagi taomlardan birini tanlang: ",reply_markup=InlineKeyboardMarkup(tugmain3))
    return 5   
def ortga(updater: Update, context: CallbackContext):
    msga = updater.message.text
    if msga=="ortga":
        updater.message.reply_text(".", reply_markup=ReplyKeyboardMarkup(tugma,resize_keyboard=True))

def help_command(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Use /start to test this bot.")
    keyboard = [InlineKeyboardButton("Test", callback_data=['1','2'])]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Please choose:', reply_markup=reply_markup)
    return 6


def main():
    TOKENT='5134189849:AAFHD88aZA8clneF6yPkEt2PWxLw1XKSstA'
    updater = Updater(TOKENT)
    all_handler = ConversationHandler(
        entry_points=[CommandHandler("start",start)],
        states= {
            1: [MessageHandler(Filters.text,familiya)],
            2: [MessageHandler(Filters.text,tugma1)],
            3: [MessageHandler(Filters.text, agar)],
            4: [MessageHandler(Filters.text, agar2)],
            5: [MessageHandler(Filters.text,ortga)],
            6: [MessageHandler(Filters.text,help_command)]
        },
        fallbacks=[]
    )
    updater.dispatcher.add_handler(all_handler)
    updater.start_polling()
    updater.idle()
    

if __name__ =="__main__":
    main()
