from telegram import Update, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove, InlineKeyboardButton, \
    InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters, ConversationHandler, \
    CallbackQueryHandler

button_in = [
    [
        InlineKeyboardButton("Lavash", callback_data="1"),
        InlineKeyboardButton("Desert", callback_data="2"),
    ],
]

button_lavash = [
    [
        InlineKeyboardButton("Lavash goshli", callback_data="1_1"),
        InlineKeyboardButton("Lavash tovuqli", callback_data="1_2"),
    ],
    [
        InlineKeyboardButton("Lavash serli", callback_data="1_3"),
    ],
    [
        InlineKeyboardButton("Ortga",callback_data="1_0")
    ]
]
button_lavgushli=[
    [
        InlineKeyboardButton("Mini Lavash",callback_data="1_1_1"),
        InlineKeyboardButton("Max Lavash",callback_data="1_1_2")
    ],
    [
        InlineKeyboardButton("Ortga",callback_data="1_1_0")
    ]
]

button_desert = [
    [
        InlineKeyboardButton("Dasert olma", callback_data="2_1"),
        InlineKeyboardButton("Dasert banan", callback_data="2_2"),
    ],
    [
        InlineKeyboardButton("Dasert olcha", callback_data="2_3"),
    ],
    [
        InlineKeyboardButton("Ortga",callback_data="2_0")
    ]
]


#
#
# button_desolma=[
#     [
#         InlineKeyboardButton("Mini Lavash",callback_data="1_1_1"),
#         InlineKeyboardButton("Max Lavash",callback_data="1_1_2")
#     ],
#     [
#         InlineKeyboardButton("Ortga",callback_data="1_1_0")
#     ]
# ]

def btn_num(k=16):
    button_lav_soni = []
    for i in range(1,16,5):
        btn = []
        for j in range(i, i+5):
            btn.append(InlineKeyboardButton(f"{j}", callback_data=f"1_1_1_{j}"))
        button_lav_soni.append(btn)

    button_lav_soni.append([InlineKeyboardButton(f"soni: {k}", callback_data=f"1_1_1_{k}")])
    button_lav_soni.append([InlineKeyboardButton(f"buyurtma yuborish: ", callback_data=f"1_1_1_ok")])
    button_lav_soni.append([InlineKeyboardButton(f"soni: ortga", callback_data=f"1_1_1_0")])
    return button_lav_soni