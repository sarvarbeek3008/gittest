from telegram import Update, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackContext, Filters, MessageHandler, ConversationHandler, CallbackQueryHandler
from new_button import *



def start(update: Update, context: CallbackContext):
    update.message.reply_text("Assalomu alaykum\n\n Ism kiriting! ")


    return 1
def name(update: Update, context: CallbackContext):
    ism = update.message.text
    user = update.message.from_user
    with open(f"{user.id}.txt", "w") as f:
        f.write(f"ID: {user.id}\nMijozni ismi: {ism}\n")
    update.message.reply_text("Fam kiriting!")



    return 2
def surname(update: Update, context: CallbackContext):
    button_lang = [
        [KeyboardButton("UZ 🇺🇿"), KeyboardButton("RUS 🇷🇺")]
    ]
    fam = update.message.text
    user = update.message.from_user
    with open(f"{user.id}.txt", "a") as f:
        f.write(f'Mijozni familasi: {fam}')
    update.message.reply_text("Tini tanlang", reply_markup=ReplyKeyboardMarkup(button_lang, resize_keyboard=True))



    return 3
def mane(update: Update, context: CallbackContext):
    button_key = [
        [KeyboardButton("🍴 Menyu")],
        [KeyboardButton("🛍 Mening buyurtmalarim")]
    ]

    update.message.reply_text("Quyidagilardan birini tanlang", reply_markup=ReplyKeyboardMarkup(button_key, resize_keyboard=True))



    return 4
def in_mane(update: Update, context: CallbackContext):


    update.message.reply_photo(photo=open("oqtepa.jpg", "rb"),
                               caption="Yetkazib berish bo'limi Toshkent shaxrida soat 10:00 dan 3:00 gacha ishlaydi",
                               reply_markup=InlineKeyboardMarkup(buttun_in))




    return 5
def button_inline(update: Update, context: CallbackContext):
    query = update.callback_query
    # print(query)
    data = query.data.split('_')
    # query.message.delete()
    # print(data)

    if data[0] == "1":
        # query.message.delete()
        query.message.reply_photo(photo=open("oqtepa.jpg", "rb"),
                                  caption="Juda aniq tanlov buldi",
                                  reply_markup=InlineKeyboardMarkup(button_la))
        if data[1] == "1":
            query.message.delete()
            query.message.reply_photo(photo=open("oqtepa.jpg","rb"), caption="Lavash goshtili qanaqasidan kerak",
                                     reply_markup=InlineKeyboardMarkup(button_lav))
            if data[2] == "1":
                # query.message.delete()
                query.message.reply_text("Nechta mini lavash Soni tanlang",
                                         reply_markup=InlineKeyboardMarkup(btn_num()))
                if int(data[3]) > 15:
                    j = int(data[3])
                    j = j + 1

                    query.message.reply_text("Nechta mini lavash Soni tanlang",
                                             reply_markup=InlineKeyboardMarkup(btn_num(j)))
            #
            #
            # elif data[2] == "2":
            #     query.message.reply_text("Nechta klassik lavash Soni tanlang",
            #                              reply_markup=InlineKeyboardMarkup(btn_num()))
            # elif data[2] == "0":
            #     query.message.delete()
            #     query.message.reply_photo(photo=open("oqtepa.jpg", "rb"),
            #                               caption="Juda aniq tanlov buldi",
            #                               reply_markup=InlineKeyboardMarkup(button_la))

        elif data[1] == '2':
            print("data2")
        elif data[1] == "3":
            print("data3")
        # elif data[1] == "0":
        #      in_mane(query, context)
        #      print("data1")

    elif data[0] == "2":
        query.message.reply_photo(photo=open("oqtepa.jpg", "rb"), caption="Juda aniq tanlov buldi",
                                  reply_markup=InlineKeyboardMarkup(button_bur))