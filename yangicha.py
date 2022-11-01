from telegram import InlineKeyboardMarkup, Update, KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters, ConversationHandler, CallbackQueryHandler

def start(updater: Update, context: CallbackContext):
    updater.message.reply_text("Assalomu alaykum bizni botimizga hush kelibsiz. ismingizni kiriting")
    return 1
def name(updater: Update, context: CallbackContext):
    user = updater.message.from_user
    ism = updater.message.text
    print(ism)
    updater.message.reply_text("Familiyangizni kiriting")
    return 2
def surname(updater: Update, context: CallbackContext):
    user = updater.message.from_user
    familiya = updater.message.text
    print(familiya)
    button_lang = [
        [KeyboardButton("uzbek")], [KeyboardButton("rus")]
    ]
    updater.message.reply_text(" ozingizga qulay bolgan tilni tanlang", reply_markup=ReplyKeyboardMarkup(button_lang,resize_keyboard=True))

    return 3
def tugma(updater: Update, context: CallbackContext):
    tugmalar = [
        [KeyboardButton("menyu")],
        [KeyboardButton("mening buyurtmalarim")],
        [KeyboardButton("fikr bildirish")],
        [KeyboardButton("sozlamalar")],
        
    ]
    updater.message.reply_text("qulay bolimni tanlang",reply_markup=ReplyKeyboardMarkup(tugmalar, resize_keyboard=True))
    msg = updater.message.text
    if msg=="menyu":
        return 4

def inline(updater: Update, context: CallbackContext):
    tugma_in = [
        [InlineKeyboardButton("lavash",callback_data="1"),
        InlineKeyboardButton("desert", callback_data="2")],
        [InlineKeyboardButton("set",callback_data="3"),
        InlineKeyboardButton("xaggi", callback_data="4")],
        [InlineKeyboardButton("burger", callback_data="5"),
        InlineKeyboardButton("pizza", callback_data="6")]
    ]
    user = updater.message.from_user
    context.bot.send_photo(user.id, photo=open("manzara.jpg.jpg","rb"),caption="yetkazib berish xizmati faqat vodiy boylab xolos",reply_markup=InlineKeyboardMarkup(tugma_in))
def main():
    TOKENT = '5376340513:AAHm4ivnWJECm1Em2rx7l-oj3DwPjjiZrhk'
    updater = Updater(TOKENT)
    all_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states = {
                1: [MessageHandler(Filters.text, name)],
                2: [MessageHandler(Filters.text, surname)],
                3: [MessageHandler(Filters.text, tugma)],
                4: [MessageHandler(Filters.text,inline)]
        },
        fallbacks=[]
    )
    updater.dispatcher.add_handler(all_handler)
    updater.start_polling()
    updater.idle()

if __name__ =="__main__":
    main()