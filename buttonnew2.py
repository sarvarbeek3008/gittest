from ctypes import resize
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup

asosiy = ReplyKeyboardMarkup([[ KeyboardButton("Kiyimlar"),KeyboardButton("Texnika")], [KeyboardButton("Oziq-Ovqat"),KeyboardButton("Sozlamalar")]],resize_keyboard=True)

kiyimlar = ReplyKeyboardMarkup([[KeyboardButton("Bahorgi"),KeyboardButton("Yozgi")],[KeyboardButton("Kuzgi"),KeyboardButton("Qishgi")],[KeyboardButton("Ortga")]],resize_keyboard=True)

texnika = ReplyKeyboardMarkup([[KeyboardButton("Televizor"),KeyboardButton("Kompyuter")],[KeyboardButton("Maishiy"),KeyboardButton("Aksesuarlar")],[KeyboardButton("Ortga")]],resize_keyboard=True)

oziq_ovqat = ReplyKeyboardMarkup([[KeyboardButton("Sabzavotlar"),KeyboardButton("Tayyor ovqatlar")],[KeyboardButton("Mevalar"),KeyboardButton("Fast-Food")],[KeyboardButton("Ortga")]],resize_keyboard=True)

sozlamalar1 = ReplyKeyboardMarkup([[KeyboardButton("Bot haqida")],[KeyboardButton("Ortga")]],resize_keyboard=True)

televizor = InlineKeyboardMarkup(
    row_width=2,
    inline_keyboard=[
        [InlineKeyboardButton("LG",callback_data="LG"),InlineKeyboardButton("Samsung",callback_data="Samsung"),InlineKeyboardButton("Lenovo",callback_data="Lenovo")],
        [InlineKeyboardButton("HP",callback_data="HP"),InlineKeyboardButton("APPLE",callback_data="APPLE"),InlineKeyboardButton("Artel",callback_data="Artel")]
    ]
)
kompyuter = InlineKeyboardMarkup(
    row_width=2,
    inline_keyboard=[
         [InlineKeyboardButton("LG",callback_data="LG"),InlineKeyboardButton("Samsung",callback_data="Samsung"),InlineKeyboardButton("Lenovo",callback_data="Lenovo")],
        [InlineKeyboardButton("HP",callback_data="HP"),InlineKeyboardButton("APPLE",callback_data="APPLE"),InlineKeyboardButton("Artel",callback_data="Artel")]
    ]
)
maishiy = InlineKeyboardMarkup(
    row_width=2,
    inline_keyboard=[
        [InlineKeyboardButton("Chang-yutgich",callback_data="Chang-yutgich"),InlineKeyboardButton("Tifal",callback_data="Tifal"),InlineKeyboardButton("Fen",callback_data="Fen")],
        [InlineKeyboardButton("Holodelnik",callback_data="Holodelnik"),InlineKeyboardButton("Muzlatgich",callback_data="Muzlatgich"),InlineKeyboardButton("Konditsoner",callback_data="Konditsoner")]
    ]
)
bahorgi = InlineKeyboardMarkup(
    row_width=2,
    inline_keyboard=[
        [InlineKeyboardButton("Spartivka",callback_data="Spartivka"),InlineKeyboardButton("Shim",callback_data="Shim")],[InlineKeyboardButton("Krasovka",callback_data="Krasovka"),InlineKeyboardButton("Jemfir",callback_data="Jemfir")]
    ]
)

yozgi =  InlineKeyboardMarkup(
    row_width=2,
    inline_keyboard=[
        [InlineKeyboardButton("Fudbolka",callback_data="Fudbolka"),InlineKeyboardButton("Sho'rtik",callback_data="Sho'rtik")],[InlineKeyboardButton("Basonochka",callback_data="Basonochka"),InlineKeyboardButton("Ko'ylak",callback_data="Ko'ylak")]
    ]
)
kuzgi =  InlineKeyboardMarkup(
    row_width=2,
    inline_keyboard=[
        [InlineKeyboardButton("Spartivka",callback_data="Spartivka"),InlineKeyboardButton("Shim",callback_data="Shim")],[InlineKeyboardButton("Krasovka",callback_data="Krasovka"),InlineKeyboardButton("Jemfir",callback_data="Jemfir")]
    ]
)
qishgi =  InlineKeyboardMarkup(
    row_width=2,
    inline_keyboard=[
        [InlineKeyboardButton("Kurtka",callback_data="Kurtka"),InlineKeyboardButton("Shim",callback_data="Shim")],[InlineKeyboardButton("Etik",callback_data="Etik"),InlineKeyboardButton("Jemfir",callback_data="Jemfir")]
    ]
)

aksesuarlar =  InlineKeyboardMarkup(
    row_width=2,
    inline_keyboard=[
        [InlineKeyboardButton("Soat",callback_data="Soat"),InlineKeyboardButton("Chexol",callback_data="Chexol")],[InlineKeyboardButton("Zanjir",callback_data="Zanjir"),InlineKeyboardButton("Steklo",callback_data="Steklo")]
    ]
)


sabzavotlar =  InlineKeyboardMarkup(
    row_width=2,
    inline_keyboard=[
        [InlineKeyboardButton("Sabzi",callback_data="Sabzi"),InlineKeyboardButton("Piyoz",callback_data="Piyoz")],[InlineKeyboardButton("Kartoshka",callback_data="Kartoshka"),InlineKeyboardButton("Karam",callback_data="Karam")]
    ]
)

mevalar =  InlineKeyboardMarkup(
    row_width=2,
    inline_keyboard=[
        [InlineKeyboardButton("Olma",callback_data="Olma"),InlineKeyboardButton("Shaftoli",callback_data="Shaftoli")],[InlineKeyboardButton("O'rik",callback_data="O'rik"),InlineKeyboardButton("Do'lana",callback_data="Do'lana")]
    ]
)

fast_food =  InlineKeyboardMarkup(
    row_width=2,
    inline_keyboard=[
        [InlineKeyboardButton("Hot-Dog",callback_data="Hot-Dog"),InlineKeyboardButton("Twister",callback_data="Twister")],[InlineKeyboardButton("Lavash",callback_data="Lavash"),InlineKeyboardButton("Burger",callback_data="Burger")]
    ]
)



