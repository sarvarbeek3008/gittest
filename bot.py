# from functools import update_wrapper
# from telegram import Update
# from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, filters

# updater='5278121475:AAGdmNeGAr3sfxSPvkL9OZIFf8bDLMMBrmk'
# def start(code: Update, context: CallbackContext):
#     code.message.reply_text(f'Assalomu alaykum {code.effective_user.first_name}')
#     user = code.message.from_user
#     print(user.id,user.link,)

#     code.message.reply_text(f"assalomu alaykum {user}. Sizga qanday yordamlarimiz kerak")

# def exo(updater: Update, context: CallbackContext):
#     msg = updater.message.txt
#     updater.message.reply_text()
# def azizbek(salom: Update, context: CallbackContext):
#     salom.message.reply_text(f"nima gap garriycha {salom.effective_user.first_name}")
# updater = Updater('5278121475:AAGdmNeGAr3sfxSPvkL9OZIFf8bDLMMBrmk')

# updater.dispatcher.add_handler(CommandHandler('start', start))
# updater.dispatcher.add_handler(CommandHandler('azizbek',azizbek))
# updater.dispatcher.add_handler(CommandHandler('exo',exo))
# updater.start_polling()
# updater.idle()
a = "yangi kod"

from telegram.ext import Updater
from telegram.ext import MessageHandler, Filters
import wikipedia as wiki 

# put your toen here
BOT_TOKEN= "5211616689:AAH1UZDJT_qUrzHP-PutiXZOZ49fz_-Opf4"

updater= Updater(BOT_TOKEN)  #Bot Token is given by BotFather on Telegram while creating bot. 
def get_wiki(word):
    try:
        return wiki.summary(word)
    except:
        return "Not Found"

def textpro(bot, update):
    msg= update.message.text.lower()
    senderName= update.message.from_user.first_name
    chatid= update.message.chat.id
    print("{}: {}".format(senderName, msg))
    if(msg.startswith('wiki')):
        bot.send_message(chat_id= chatid,text= get_wiki(msg[5:]))
        print("Bot: Wikipedia summery of {}".format(msg[5:]))
    else:
        bot.send_message(chat_id= chatid, text= "{}, Invalid command".format(senderName))
        print("Bot: Invalid command")

updater.dispatcher.add_handler(MessageHandler(Filters.text, textpro))
updater.start_polling()
print("Bot Server Started")
updater.idle()



