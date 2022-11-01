from aiogram.types import KeyboardButton, ReplyKeyboardMarkup



tugmakeyboard = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton("Test", request_contact=True),
            KeyboardButton("test 2", request_location=True)
        ]
    ],
    resize_keyboard=True
)

tugmakeyboard2 = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton("")
        ]
    ]
)