from telegram import Update, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters, ConversationHandler,CallbackQueryHandler

from BOT_2_1 import *

def start(updater:Update,context:CallbackContext):
    # user = updater.message.from_user
    updater.message.reply_text("Assalomu alaykum \n \n Ismingizni kiriting  ✍")


    return 1
def name(updater:Update,context:CallbackContext):
    user=updater.message.from_user
    ism=updater.message.text
    print(ism)
    updater.message.reply_text("Familiyangizni yozing ✍️")

    return 2
def surname(updater:Update,context:CallbackContext):
    button_lang=[
        [KeyboardButton("O'zbek"),KeyboardButton("Rus")]
    ]
    user=updater.message.from_user
    fam=updater.message.text
    print(fam)
    updater.message.reply_text("Tilni tanlang!",reply_markup=ReplyKeyboardMarkup(button_lang,resize_keyboard=True))


    return 3
def menu(updater:Update,context:CallbackContext):
    button_info=[
        [KeyboardButton("Menyu "),KeyboardButton("Mening buyurtmalarim")],
        [KeyboardButton("Fikr bildiring"),KeyboardButton("Sozlamalar")],
        # [KeyboardButton("Sozlamalar")]
    ]
    updater.message.reply_text("Quyidagilardan birini tanlang",reply_markup=ReplyKeyboardMarkup(button_info,resize_keyboard=True))


        # updater.message.reply_text("Menyu")
    return 4

def menu_main(updater:Update,context:CallbackContext):
    updater.message.reply_photo(photo=open("fastfood.jpg", "rb"), caption="Yetkazib berish xizmati mavjud",
                                reply_markup=InlineKeyboardMarkup(button_in))
    # msg = updater.message.text
    # if msg == "Menyu":
        # button_in = [
        #     [
        #         InlineKeyboardButton("Lavash", callback_data="Lavash"),
        #         InlineKeyboardButton("Desert", callback_data=2)
        #     ]
        # ]
        # user = updater.message.from_user
        # context.bot.send_photo(user.id, photo=open("804201997_8143.jpg", "rb"),
        #                        caption="Yetkazib berish xizmati mavjud", reply_markup=InlineKeyboardMarkup(button_in))


    return 5

def inline_button(update:Update,context:CallbackContext):
    query= update.callback_query
    # print(query)
    data=query.data.split('_')
    print(data)
    if data[0]=="1":
        query.message.delete()
        query.message.reply_photo(photo=open("lavashgushli.jpg", "rb"), caption="Juda aniq tanlov bo'ldi", reply_markup=InlineKeyboardMarkup(button_lavash))
        if data[1]=="1":
            query.message.delete()
            query.message.reply_photo(photo=open("lavashgushli.jpg", "rb"), caption="Lavash go'shtli tanlandi ", reply_markup=InlineKeyboardMarkup(button_lavgushli))
            print("data 1")
            if data[2]=="1":
                query.message.delete()
                query.message.reply_text("Nechta mini lavash olmoqchisiz",reply_markup=InlineKeyboardMarkup(btn_num()))

                if int(data[3])>15:
                    query.message.delete()
                    j=int(data[3])
                    j=j+1
                    query.message.reply_text("Nechta mini lavash olmoqchisiz",reply_markup=InlineKeyboardMarkup(btn_num(j)))
                elif data[3]==17:
                    query.message.reply_text("Buyurtmangiz qabul qilindi")
        elif query.data=="2":
            query.message.delete()
            query.message.reply_photo(photo=open("lavashgushli.jpg", "rb"), caption="Lavash tovuqli tanlandi ",
                                      reply_markup=InlineKeyboardMarkup(button_lavtovuqli))
            print("data 2")
        elif data[1]=="3":
            query.message.delete()
            query.message.reply_photo(photo=open("lavashgushli.jpg", "rb"), caption="Lavash sirli tanlandi ",
                                      reply_markup=InlineKeyboardMarkup(button_lavsirli))
            print("data 3")
        elif data[1]=="4":
            query.message.reply_photo(photo=open("lavashgushli.jpg", "rb"), caption="Ortga ",
                                      reply_markup=InlineKeyboardMarkup(button_in))
        # elif data[1]=="0":
        # 992646262
        #     in_mane(query,context)
        #     print("data 1")
            # query.message.delete()
            # query.message.reply_text("Lavash gushli" )
    elif data[0]=="2":
        query.message.reply_photo(photo=open("fruit.jpg", "rb"), caption="Juda aniq tanlov bo'ldi", reply_markup=InlineKeyboardMarkup(button_desert))
        if data[1]=="1":
            print("salom")
        elif data[1]=="2":
            print("data 2")
        elif data[1]=="3":
            print("data 3")

def main():
    TOKEN="5365718474:AAGWmEwCALaCXi_0baVoP3eQo6qvAtHmkLs"

    updater=Updater(TOKEN)

    all_handler=ConversationHandler(
        entry_points=[CommandHandler("start",start)],
        states={
            1:[MessageHandler(Filters.text,name)],
            2:[MessageHandler(Filters.text,surname)],
            3:[MessageHandler(Filters.text,menu)],
            4:[MessageHandler(Filters.regex('^(Menyu)$'),menu_main)],
            5:[CallbackQueryHandler(inline_button)],
            # 6: [CallbackQueryHandler(inline_lavash)],
            # 6:[CallbackQueryHandler(inline_lavash)],
        },
        fallbacks=[]
    )
    updater.dispatcher.add_handler(all_handler)
    updater.start_polling()
    updater.idle()
main()

if __name__ == "__main__":
    main()


















#
# ,d czx c.,xcfd











# from telegram import Update, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove, InlineKeyboardButton, \
#     InlineKeyboardMarkup
# from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters, ConversationHandler, \
#     CallbackQueryHandler
#
#
#
# def start(updete: Update, context: CallbackContext):
#     updete.message.reply_text("Assalomu aleykum \n\n Ismi kiriteng! ")
#
#
#
#     return 1
# def name(updater: Update, context: CallbackContext):
#     updater.message.reply_text("familliya kiriting")
#     ism = updater.message.from_user
#
#     return 2
# def surname(updater: Update, context: CallbackContext):
#     info_button = [
#         [KeyboardButton("➡️Oldinga"), KeyboardButton("️⬅️Ortga")]
#     ]
#     # updater.message.reply_text("familliya yozing")
#     familliya = updater.message.from_user
#     updater.message.reply_text("Endi nima qilasiz", reply_markup=ReplyKeyboardMarkup(info_button))
#
#     return 3
# def Texnik(updater: Update, context: CallbackContext):
#     button_menu = [
#         [KeyboardButton("Texnikalar 🛠")],
#         [KeyboardButton("Kiyimlar 👔"), KeyboardButton("Mashinalar 🚘"),]
#
#     ]
#     updater.message.reply_text("Quyidagilarni birini tanlang!!!", reply_markup=ReplyKeyboardMarkup(button_menu, resize_keyboard=True))
#
#
# def main():
#     TOKENT = "5365718474:AAGWmEwCALaCXi_0baVoP3eQo6qvAtHmkLs"
#
#     updater = Updater(TOKENT)
#
#     all_handler = ConversationHandler(
#         entry_points=[CommandHandler("start", start)],
#         states = {
#             1: [MessageHandler(Filters.text, name)],
#             2: [MessageHandler(Filters.text, surname)],
#             3: [MessageHandler(Filters.text, Texnik)]
#
#
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
#
