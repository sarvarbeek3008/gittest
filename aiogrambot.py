# import logging
# from aiogram import Bot, Dispatcher, executor, types
# from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
# from button import tugmakeyboard
# from aiogram.types import ReplyKeyboardRemove,ReplyKeyboardMarkup, KeyboardButton,InlineKeyboardMarkup, InlineKeyboardButton


# API_TOKEN = '5315273864:AAERM9NviDlv-VaW_nh7AmOMWh90w8zDjfM'
# logging.basicConfig(level=logging.INFO)
# bot = Bot(token=API_TOKEN)
# dp = Dispatcher(bot)


# tugma = KeyboardButton("option1","option2","option3","option 4")
# tugmain = InlineKeyboardButton("sarvarbek",callback_data="jakbarov")

# tugma_new = InlineKeyboardMarkup(
#     row_width=2,
#     inline_keyboard=[
#         [InlineKeyboardButton("test", callback_data="test")],
#         #[InlineKeyboardButton("tuh")]
#     ]
# )
# @dp.message_handler(commands=['start'])
# async def process_start_command(message: types.Message):
#     await message.reply("Привет!", reply_markup=tugma_new)

# @dp.callback_query_handler(text="test")
# async def call_test(call: types.CallbackQuery):
#     await call.message.answer("salom", reply_markup=tugmakeyboard)    
#     await call.message.delete()
#     await call.answer(cache_time=60)

# @dp.message_handler()
# async def eko(message: types.Message):
#     await message.reply(message.text)
#     if message.text=="option1":
#         await message.answer("tugmalardan birini tanlang ", reply_markup=tugma_new)


# if __name__ == '__main__':
#     executor.start_polling(dp, skip_updates=True)