from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

b1 = KeyboardButton("// Rejim 1")
b2 = KeyboardButton("// Rejim 2")
b3 = KeyboardButton("// Rejim 3")

kb_klient = ReplyKeyboardMarkup()
kb_klient.add(b1).add(b2).add(b3)