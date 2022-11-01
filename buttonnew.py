
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup 
tugmain = InlineKeyboardMarkup(
    row_width=2,
    inline_keyboard=[
        [InlineKeyboardButton("UZ", callback_data="UZ")],
        [InlineKeyboardButton("ENG", callback_data="ENG")],
        [InlineKeyboardButton("RUS",callback_data="RUS")]
    ]
)

tugmauz = ReplyKeyboardMarkup([
    [KeyboardButton("Menyu"),KeyboardButton("Fikr Bildirish 📝")], [KeyboardButton("Sozlamalar ⚙️"), KeyboardButton("Buyurtmalaringiz")]],resize_keyboard=True
)
tugmaru = ReplyKeyboardMarkup(
    [KeyboardButton("МЕНЮ"), KeyboardButton("КОММЕНТАРИИ"), KeyboardButton("НАСТРОЙКИ"), KeyboardButton("ЗАКАЗЫ")]
)
tugmaeng = ReplyKeyboardMarkup(
    [KeyboardButton("MENU"),KeyboardButton("COMMENTS"), KeyboardButton("OPTIONS"), KeyboardButton("ORDER")]
)

tugma1 = ReplyKeyboardMarkup([
    [KeyboardButton("Fast-Food 🌭"), KeyboardButton("🍾 Ichimliklar"), KeyboardButton("NEW// Milliy taomlar")],[KeyboardButton("Ortga")]], resize_keyboard=True
)

tugmafastfood = InlineKeyboardMarkup(
    row_width=3,
    inline_keyboard=[
        [InlineKeyboardButton("🌭 Hot-Dog", callback_data="Hot-Dog")],
        [InlineKeyboardButton("🫔 Twister", callback_data="Twister")],
        [InlineKeyboardButton("🫔 Lavash", callback_data="Lavash")],
        [InlineKeyboardButton("🍕 Pizza", callback_data="Pizza")],
        [InlineKeyboardButton("🍔 Humburger", callback_data="Humburger")]
    ]
)

tugmaichimliklar = InlineKeyboardMarkup(
    row_width=3,
    inline_keyboard=[
    [InlineKeyboardButton("Pepsi 🍷",callback_data="Pepsi")],
    [InlineKeyboardButton("Coca-Cola 🍷", callback_data="Coca-Cola")],
    [InlineKeyboardButton("Fanta 🧋", callback_data="Fanta")],
    [InlineKeyboardButton("Energetics 〽️", callback_data="Energetics")]
    ])
tugmamilliytaomlar = InlineKeyboardMarkup(
    row_width=2,
    inline_keyboard=[
        [InlineKeyboardButton("Osh", callback_data="osh")],
        [InlineKeyboardButton("Mastava", callback_data="Mastava")],
        [InlineKeyboardButton("Sho'rva",callback_data="Sho'rva")],
        [InlineKeyboardButton("Kebab", callback_data="Kebab")]
    ]
)

tugma_options = ReplyKeyboardMarkup([
    [KeyboardButton("Ozingiz haqingizda malumotlar"),
    KeyboardButton("Ortga")]],resize_keyboard=True
)

registratsiya = ReplyKeyboardMarkup(
[
    
        [KeyboardButton("Raqmingizni yuborish", request_contact=True)],
        [KeyboardButton("Lokatsiyani yuborish", request_location=True)],
        [KeyboardButton("Bosh menyuga o'tish")]

    
], resize_keyboard=True)

registet  = ReplyKeyboardMarkup([
   [ KeyboardButton("Ro'yhatdan o'tish"),
    KeyboardButton("Menyuga o'tish")]
], resize_keyboard=True)



