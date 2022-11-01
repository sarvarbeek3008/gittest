# from email import message
# from email.message import Message
# import logging
# from aiogram import Bot, Dispatcher, executor, types
# from aiogram.types import KeyboardButton,InlineKeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove, InlineKeyboardMarkup
# from buttonnew import tugmain,tugmaru,tugmamilliytaomlar,tugma1,tugma_options,tugmaeng,tugmafastfood,tugmaichimliklar,tugmauz,registratsiya,registet
# from aiogrambot import API_TOKEN
# from texts import texts

# API_TOKEN = '5364625104:AAHzIV7hhHfz7-2X4U4TPOAY4pLqSW4uJqY'
# logging.basicConfig(level=logging.INFO)

# bot = Bot(token=API_TOKEN, parse_mode="html")
# dp = Dispatcher(bot)

# @dp.message_handler(commands=['start'])
# async def boshlash(message: types.Message):
#     await message.reply(f"Assalomu alaykum bizni birinchi botimizga hush kelibsiz. \n Iltimos tilni tanlang"
#     f"{texts['uz_start']}", reply_markup=registet)
# @dp.callback_query_handler(text="Ro'yhatdan o'tish")
# async def royhat(call: types.CallbackQuery):
#     await call.message.reply("Ro'yhatdan o'ting",reply_markup =registratsiya)
# @dp.callback_query_handler(text="Kontaktingizni yuboring")
# async def kontakt(call: types.CallbackQuery):
#     await call.message.reply("Tilni Tanlang", reply_markup=tugmain)
# # @dp.message_handler(content_types=types.ContentType.TEXT)
# # async def agar(message: types.Message):
# #     xabar = message.text
# #     if xabar=="UZ":
# #         await message.answer("Bo'limlardan birini tanlang", reply_markup=tugmauz)
# #     if xabar == "RUS":
# #         await message.reply("Выберите один из разделов", reply_markup=tugmaru)
# #     if xabar=="ENG":
# #         await message.answer("Select one of the sections")

# @dp.callback_query_handler(text="UZ")
# async def uzbek_menu(call: types.CallbackQuery):
#     await call.message.answer("Quyidagi bo'limlardan birini tanlang:", reply_markup=tugmauz)
#     await call.message.delete()
#     await call.answer(cache_time=60)
# @dp.callback_query_handler(text="RUS")
# async def uzbek_menu1(call: types.CallbackQuery):
#     await call.message.reply("выбрать один из разделов",reply_markup=tugmaru)
#     await call.message.delete()
#     await call.answer(cache_time=60)
# @dp.callback_query_handler(text="ENG")
# async def uzbek_menu2(call: types.CallbackQuery):
#     await call.message.answer("..",reply_markup=tugmaeng)
#     await call.message.delete()
#     await call.answer(cache_time=60)
# @dp.message_handler(text="Menyu")
# async def agar2(message: types.Message):
#         await message.answer("Buyurtma berishingiz mumkin", reply_markup=tugma1, parse_mode="HTML")
# @dp.message_handler(text="Fikr Bildirish 📝")
# async def agar3(message: types.Message):
#     await message.answer("Fikringizni @Djakbarov ga yozib qoldirishingiz mumkin")
# @dp.message_handler(text="Sozlamalar ⚙️")
# async def sozlamalar(message: types.Message):
#     await message.answer("Ma'lumotlaringizni bilmoqchimisiz",reply_markup=tugma_options,parse_mode="Html")
# @dp.message_handler(content_types=types.ContentType.TEXT)
# async def agar3(message: types.Message):
#     xabar2 = message.text
#     if xabar2 == "Fast-Food 🌭":
#         await message.reply("Fast-Food lardan biriga buyurtma berishingiz mumkin <a href='https://telegra.ph/file/f41b4f41a4a50e9ec38ca.png'> </a>tanlang:", reply_markup=tugmafastfood, parse_mode="HTML")
#     if xabar2=="🍾 Ichimliklar":
#         await message.reply("<a href='https://telegra.ph/file/4a6769fa52882833d5dd2.png'> </a> Ichimliklardan birini tanlang", reply_markup=tugmaichimliklar, parse_mode="HTML")
#     if xabar2=="NEW// Milliy taomlar":
#         await message.reply("<a href='https://telegra.ph/file/a568b2a36d015081e3879.png'> </a> Millliy taomlardan birini tanlang",reply_markup=tugmamilliytaomlar, parse_mode="HTML")
#     if xabar2=="Ortga":
#         await message.reply("Bo'limlardan birini tanlang: ", reply_markup=tugmauz)
#     if xabar2=="Ozingiz haqingizda malumotlar":
#         await message.reply(message.from_user.full_name)
#     if xabar2 == "Ro'yhatdan o'tish":
#         await message.reply("Ro'yhatdan o'ting",reply_markup =registratsiya)
#     if xabar2=="Kontaktingizni yuboring":
#         await message.reply("Menyuni tanlang", reply_markup=tugmauz)
#     if xabar2=="Menyuga o'tish":
#         await message.reply("Bo'limlardan bbirni tanlang", reply_markup=tugmauz)
#     if xabar2=="Buyurtmalaringiz":
#         await message.reply("Siz hali hech narsa buyurtma qilmadingiz")
# @dp.callback_query_handler(text="")
# async def hot_dog(call: types.CallbackQuery):
#     await call.message.answer("")
# if __name__ =="__main__":
#     executor.start_polling(dp, skip_updates=True)from email import message
# from email.message import Message
# import logging
# from aiogram import Bot, Dispatcher, executor, types
# from aiogram.types import KeyboardButton,InlineKeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove, InlineKeyboardMarkup
# from buttonnew import tugmain,tugmaru,tugmamilliytaomlar,tugma1,tugma_options,tugmaeng,tugmafastfood,tugmaichimliklar,tugmauz,registratsiya,registet
# from aiogrambot import API_TOKEN
# from texts import texts

# API_TOKEN = '5364625104:AAHzIV7hhHfz7-2X4U4TPOAY4pLqSW4uJqY'
# logging.basicConfig(level=logging.INFO)

# bot = Bot(token=API_TOKEN, parse_mode="html")
# dp = Dispatcher(bot)

# @dp.message_handler(commands=['start'])
# async def boshlash(message: types.Message):
#     await message.reply(f"Assalomu alaykum bizni birinchi botimizga hush kelibsiz. \n Iltimos tilni tanlang"
#     f"{texts['uz_start']}", reply_markup=registet)
# @dp.callback_query_handler(text="Ro'yhatdan o'tish")
# async def royhat(call: types.CallbackQuery):
#     await call.message.reply("Ro'yhatdan o'ting",reply_markup =registratsiya)
# @dp.callback_query_handler(text="Kontaktingizni yuboring")
# async def kontakt(call: types.CallbackQuery):
#     await call.message.reply("Tilni Tanlang", reply_markup=tugmain)
# # @dp.message_handler(content_types=types.ContentType.TEXT)
# # async def agar(message: types.Message):
# #     xabar = message.text
# #     if xabar=="UZ":
# #         await message.answer("Bo'limlardan birini tanlang", reply_markup=tugmauz)
# #     if xabar == "RUS":
# #         await message.reply("Выберите один из разделов", reply_markup=tugmaru)
# #     if xabar=="ENG":
# #         await message.answer("Select one of the sections")

# @dp.callback_query_handler(text="UZ")
# async def uzbek_menu(call: types.CallbackQuery):
#     await call.message.answer("Quyidagi bo'limlardan birini tanlang:", reply_markup=tugmauz)
#     await call.message.delete()
#     await call.answer(cache_time=60)
# @dp.callback_query_handler(text="RUS")
# async def uzbek_menu1(call: types.CallbackQuery):
#     await call.message.reply("выбрать один из разделов",reply_markup=tugmaru)
#     await call.message.delete()
#     await call.answer(cache_time=60)
# @dp.callback_query_handler(text="ENG")
# async def uzbek_menu2(call: types.CallbackQuery):
#     await call.message.answer("..",reply_markup=tugmaeng)
#     await call.message.delete()
#     await call.answer(cache_time=60)
# @dp.message_handler(text="Menyu")
# async def agar2(message: types.Message):
#         await message.answer("Buyurtma berishingiz mumkin", reply_markup=tugma1, parse_mode="HTML")
# @dp.message_handler(text="Fikr Bildirish 📝")
# async def agar3(message: types.Message):
#     await message.answer("Fikringizni @Djakbarov ga yozib qoldirishingiz mumkin")
# @dp.message_handler(text="Sozlamalar ⚙️")
# async def sozlamalar(message: types.Message):
#     await message.answer("Ma'lumotlaringizni bilmoqchimisiz",reply_markup=tugma_options,parse_mode="Html")
# @dp.message_handler(content_types=types.ContentType.TEXT)
# async def agar3(message: types.Message):
#     xabar2 = message.text
#     if xabar2 == "Fast-Food 🌭":
#         await message.reply("Fast-Food lardan biriga buyurtma berishingiz mumkin <a href='https://telegra.ph/file/f41b4f41a4a50e9ec38ca.png'> </a>tanlang:", reply_markup=tugmafastfood, parse_mode="HTML")
#     if xabar2=="🍾 Ichimliklar":
#         await message.reply("<a href='https://telegra.ph/file/4a6769fa52882833d5dd2.png'> </a> Ichimliklardan birini tanlang", reply_markup=tugmaichimliklar, parse_mode="HTML")
#     if xabar2=="NEW// Milliy taomlar":
#         await message.reply("<a href='https://telegra.ph/file/a568b2a36d015081e3879.png'> </a> Millliy taomlardan birini tanlang",reply_markup=tugmamilliytaomlar, parse_mode="HTML")
#     if xabar2=="Ortga":
#         await message.reply("Bo'limlardan birini tanlang: ", reply_markup=tugmauz)
#     if xabar2=="Ozingiz haqingizda malumotlar":
#         await message.reply(message.from_user.full_name)
#     if xabar2 == "Ro'yhatdan o'tish":
#         await message.reply("Ro'yhatdan o'ting",reply_markup =registratsiya)
#     if xabar2=="Kontaktingizni yuboring":
#         await message.reply("Menyuni tanlang", reply_markup=tugmauz)
#     if xabar2=="Menyuga o'tish":
#         await message.reply("Bo'limlardan bbirni tanlang", reply_markup=tugmauz)
#     if xabar2=="Buyurtmalaringiz":
#         await message.reply("Siz hali hech narsa buyurtma qilmadingiz")
# @dp.callback_query_handler(text="")
# async def hot_dog(call: types.CallbackQuery):
#     await call.message.answer("")
# if __name__ =="__main__":
#     executor.start_polling(dp, skip_updates=True)