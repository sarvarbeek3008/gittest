import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import KeyboardButton,InlineKeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove, InlineKeyboardMarkup

from aiogrambot import API_TOKEN
from buttonnew2 import asosiy,kiyimlar,kuzgi,kompyuter,bahorgi,qishgi,yozgi,texnika,televizor,maishiy,mevalar,asosiy,oziq_ovqat,sozlamalar1,sabzavotlar,fast_food,aksesuarlar
from buttonnew import tugmain,registratsiya

API_TOKEN = '5350705889:AAE6KIK0McxXO92rxD0KdDjbYGmZCV6h0o4'
logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN, parse_mode="HTML")
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def boshlash(message: types.Message):
    await message.reply(f"Assalomu alaykum bizni birinchi botimizga hush kelibsiz. \n Iltimos tilni tanlang",reply_markup= tugmain)


@dp.callback_query_handler(text="UZ")
async def uzbek_menu(call: types.CallbackQuery):
    await call.message.answer("Quyidagi bo'limlardan birini tanlang // \nXavfsizligingiz uchun iltimos kontaktingizni biz bilan  ulashing :", reply_markup=registratsiya)
    await call.message.delete()
    await call.answer(cache_time=60)
@dp.message_handler(content_types=types.ContentType.TEXT)
async def agar3(message: types.Message):
    x = message.text
    if x=="Bosh menyuga o'tish":
        await message.reply("Bo'limlardan birini tanlang", reply_markup=asosiy)
    if x=="Kiyimlar":
        await message.reply("Bo'limlardan birini tanlang", reply_markup=kiyimlar)
    if x=="Texnika":
        await message.reply("Bo'limlardan birini tanlang", reply_markup=texnika)
    if x=="Oziq-Ovqat":
        await message.reply("Bo'limlardan birini tanlang", reply_markup=oziq_ovqat)
    if x=="Sozlamalar":
        await message.reply("Bo'limlardan birini tanlang", reply_markup=sozlamalar1)
    if x=="Bahorgi":
        await message.reply("Bo'limlardan birini tanlang", reply_markup=bahorgi)
    if x=="Ortga":
        await message.reply("Bo'limlardan birini tanlang", reply_markup=asosiy)
    if x=="Sabzavotlar":
         await message.reply("Bo'limlardan birini tanlang", reply_markup=sabzavotlar)
    if x=="Mevalar":
        await message.reply("Bo'limlardan birini tanlang", reply_markup=mevalar)
    if x=="Fast-Food":
        await message.reply("Bo'limlardan birini tanlang", reply_markup=fast_food)
    if x=="Yozgi":
         await message.reply("Bo'limlardan birini tanlang", reply_markup=yozgi)
    if x=="Kuzgi":
        await message.reply("Bo'limlardan birini tanlang", reply_markup=kuzgi)
    if x=="Qishgi":
         await message.reply("Bo'limlardan birini tanlang", reply_markup=qishgi)
    if x=="Kompyuter":
         await message.reply("Bo'limlardan birini tanlang", reply_markup=kompyuter)
    if x=="Televizor":
        await message.reply("Bo'limlardan birini tanlang", reply_markup=televizor)
    if x=="Aksesuarlar":
        await message.reply("Bo'limlardan birini tanlang", reply_markup=aksesuarlar)
    if x=="Maishiy":
        await message.reply("Bo'limlardan birini tanlang", reply_markup=maishiy)
    if x=="Bot haqida":
        await message.answer("Bu bot sizga masofadan turib turli narsalar sotib olish imkonini beradi\n Creator: @Djakbarov")

@dp.callback_query_handler(text="Samsung")
async def samsung(call: types.CallbackQuery):
    await call.message.answer("<a href='https://telegra.ph/file/7f940b8954e4a55d967c5.jpg'> </a> Ekran 600x1200 // Narxi 200$ ")
    await call.message.delete()
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Spartivka")
async def spartivka(call: types.CallbackQuery):
    await call.message.answer("<a href='https://telegra.ph/file/4efb000d35353ce80018a.jpg'> Spartivka // Turkiya // 20$ </a> Ekran 600x1200")
    await call.message.delete()
    await call.answer(cache_time=60)



@dp.callback_query_handler(text="Shim")
async def shim(call: types.CallbackQuery):
    await call.message.answer("<a href='https://telegra.ph/file/380f4e3bacc797123c162.jpg'> </a> Shim Turkiya // Narxi  20$ ")
    await call.message.delete()
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Krasovka")
async def krasovka(call: types.CallbackQuery):
    await call.message.answer("<a href='https://telegra.ph/file/a5f9bb1860ba282ca3161.jpg'> </a> Krasovka // Narxi 25$")
    await call.message.delete()
    await call.answer(cache_time=60)
@dp.callback_query_handler(text="Jemfir")
async def jemfir(call: types.CallbackQuery):
    await call.message.answer("<a href='https://telegra.ph/file/772d63f54b2e4c0ca61c1.jpg'> </a> Jemfir // Narxi 15$")
    await call.message.delete()
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Fudbolka")
async def fudbolka(call: types.CallbackQuery):
    await call.message.answer("<a href='https://telegra.ph/file/772d63f54b2e4c0ca61c1.jpg'> </a> Fudbolka // Narxi 10$")
    await call.message.delete()
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Sho'rtik")
async def shortik(call: types.CallbackQuery):
    await call.message.answer("<a href='https://telegra.ph/file/c53a635542305f655e4a4.jpg'> </a> Sho'rtik // Narxi 10$")
    await call.message.delete()
    await call.answer(cache_time=60)
@dp.callback_query_handler(text="Basonochka")
async def basanochka(call: types.CallbackQuery):
    await call.message.answer(" Basanochka Narxi // 10$ <a href='https://telegra.ph/file/a2ef06a828d037d12d58d.jpg'> </a> .")
    await call.message.delete()
    await call.answer(cache_time=60)
@dp.callback_query_handler(text="Ko'ylak")
async def koylak(call: types.CallbackQuery):
    await call.message.answer("Erkaklar Ko'ylagi Narxi // 10$  <a href='https://telegra.ph/file/6c7f7766fbef5bb6fb5ff.jpg'> </a>. ")
    await call.message.delete()
    await call.answer(cache_time=60)
@dp.callback_query_handler(text="Kurtka")
async def kurtka(call: types.CallbackQuery):
    await call.message.answer(" Kurtka Narxi // 20$  <a href='https://telegra.ph/file/adb4bc4f6001d8065c5b1.jpg'> </a> .")
    await call.message.delete()
    await call.answer(cache_time=60)
@dp.callback_query_handler(text="Etik")
async def etik(call: types.CallbackQuery):
    await call.message.answer("  Etik Narxi 40$ <a href='https://telegra.ph/file/370a1fd87379e7d662384.jpg'> </a> .")
    await call.message.delete()
    await call.answer(cache_time=60)
@dp.callback_query_handler(text="LG")
async def lg(call: types.CallbackQuery):
    await call.message.answer("<a href='https://telegra.ph/file/7f940b8954e4a55d967c5.jpg'> </a> Ekran 600x1200")
    await call.message.delete()
    await call.answer(cache_time=60)
@dp.callback_query_handler(text="Lenovo")
async def lenovo(call: types.CallbackQuery):
    await call.message.answer("<a href='https://telegra.ph/file/7f940b8954e4a55d967c5.jpg'> </a> Ekran 600x1200")
    await call.message.delete()
    await call.answer(cache_time=60)
@dp.callback_query_handler(text="HP")
async def hp(call: types.CallbackQuery):
    await call.message.answer(" HP Televizor Narxi 600$ <a href='https://telegra.ph/file/ae931b385baa64b67b40d.jpg'> </a>. ")
    await call.message.delete()
    await call.answer(cache_time=60)
@dp.callback_query_handler(text="APPLE")
async def apple(call: types.CallbackQuery):
    await call.message.answer("  APPLE Televizor Narxi // 1000$ <a href='https://telegra.ph/file/85160c3d2f8bcad3a62a9.jpg'> </a>. ")
    await call.message.delete()
    await call.answer(cache_time=60)
@dp.callback_query_handler(text="Artel")
async def artel(call: types.CallbackQuery):
    await call.message.answer(" Televizor Artel Narxi // 200$ <a href='https://telegra.ph/file/3ab68a91758eca1d3d3a2.jpg'> </a>. ")
    await call.message.delete()
    await call.answer(cache_time=60)
@dp.callback_query_handler(text="Chang-yutgich")
async def chang(call: types.CallbackQuery):
    await call.message.answer(" Chang yutgich Narxi // 100$ <a href='https://telegra.ph/file/e4d1b1e0bba2ad1ed4bcb.jpg'> </a>. ")
    await call.message.delete()
    await call.answer(cache_time=60)
@dp.callback_query_handler(text="Tifal")
async def tifal(call: types.CallbackQuery):
    await call.message.answer(" Elektr choynak Narxi //<a href='https://telegra.ph/file/f425e5978863fdb4f22a4.jpg'> </a>10$")
    await call.message.delete()
    await call.answer(cache_time=60)
@dp.callback_query_handler(text="Soat")
async def soat(call: types.CallbackQuery):
    await call.message.answer("Qo'l uchun soat Narxi // 20$  <a href='https://telegra.ph/file/cef3938926d188b7657c0.jpg'> </a> .")
    await call.message.delete()
    await call.answer(cache_time=60)
@dp.callback_query_handler(text="Chexol")
async def chexol(call: types.CallbackQuery):
    await call.message.answer(" Tel uchun chexol Narxi // 3$ <a href='https://telegra.ph/file/a55678ffe95ca9af0cdee.jpg'> </a> .")
    await call.message.delete()
    await call.answer(cache_time=60)
@dp.callback_query_handler(text="Zanjir")
async def zanjir(call: types.CallbackQuery):
    await call.message.answer("Zanjir Kumush Narxi // 20$  <a href='https://telegra.ph/file/74a9ce044e50d4638751a.jpg'> </a> .")
    await call.message.delete()
    await call.answer(cache_time=60)
@dp.callback_query_handler(text="Steklo")
async def steklo(call: types.CallbackQuery):
    await call.message.answer("Steklo Narxi Tel Uchun Universal// 1$  <a href='https://telegra.ph/file/dcff36346c5297b5f214b.jpg'> </a> .")
    await call.message.delete()
    await call.answer(cache_time=60)
@dp.callback_query_handler(text="Sabzi")
async def sabzi(call: types.CallbackQuery):
    await call.message.answer(" Sabzi Narxi // 0.2$ <a href='https://telegra.ph/file/5f88f88a5dd462b59d524.jpg'> </a> .")
    await call.message.delete()
    await call.answer(cache_time=60)
@dp.callback_query_handler(text="Piyoz")
async def piyoz(call: types.CallbackQuery):
    await call.message.answer("  Piyoz Narxi // 0.2$ <a href='https://telegra.ph/file/c61fbf6e23332ced5909f.jpg'> </a> .")
    await call.message.delete()
    await call.answer(cache_time=60)
@dp.callback_query_handler(text="Kartoshka")
async def kartoshka(call: types.CallbackQuery):
    await call.message.answer("<a href='https://telegra.ph/file/3597fda34df6943c76d86.jpg'> </a> Kartoshka Narxi 0.5$")
    await call.message.delete()
    await call.answer(cache_time=60)
@dp.callback_query_handler(text="Karam")
async def karam(call: types.CallbackQuery):
    await call.message.answer("<a href='https://telegra.ph/file/228f525ce528d7fcd23f8.jpg'> </a> Karam Narxi // 0.7$")
    await call.message.delete()
    await call.answer(cache_time=60)
@dp.callback_query_handler(text="Olma")
async def olma(call: types.CallbackQuery):
    await call.message.answer("<a href='https://telegra.ph/file/32bc1775a943c5eac6552.jpg'> </a> Shaftoli Narxi // 2$")
    await call.message.delete()
    await call.answer(cache_time=60)
@dp.callback_query_handler(text="Shaftoli")
async def shaftoli(call: types.CallbackQuery):
    await call.message.answer("<a href='https://telegra.ph/file/7d20cf083beabf8b17204.jpg'> </a> Shaftoli Narxi // 2$")
    await call.message.delete()
    await call.answer(cache_time=60)
@dp.callback_query_handler(text="O'rik")
async def orik(call: types.CallbackQuery):
    await call.message.answer("<a href='https://telegra.ph/file/7d20cf083beabf8b17204.jpg'> </a> O'rik Narxi // 1 kg 1$")
    await call.message.delete()
    await call.answer(cache_time=60)
@dp.callback_query_handler(text="Do'lana")
async def dolana(call: types.CallbackQuery):
    await call.message.answer("<a href='https://telegra.ph/file/814039a2bbbc77d22319f.jpg'> </a> Narxi // 1 kg  0.7$")
    await call.message.delete()
    await call.answer(cache_time=60)
@dp.callback_query_handler(text="Hot-Dog")
async def hotdog(call: types.CallbackQuery):
    await call.message.answer("<a href='https://telegra.ph/file/7f940b8954e4a55d967c5.jpg'> </a> hotdog // narxi 1$")
    await call.message.delete()
    await call.answer(cache_time=60)
@dp.callback_query_handler(text="Twister")
async def twister(call: types.CallbackQuery):
    await call.message.answer("<a href='https://telegra.ph/file/d6ebda104eb843ad280a4.jpg'> </a> Twister // 2%")
    await call.message.delete()
    await call.answer(cache_time=60)
@dp.callback_query_handler(text="Lavash")
async def lavash(call: types.CallbackQuery):
    await call.message.answer("<a href='https://telegra.ph/file/1c5ce3521ffbf7ba26e10.jpg'> </a> Lavash // 2$")
    await call.message.delete()
    await call.answer(cache_time=60)
@dp.callback_query_handler(text="Burger")
async def burger(call: types.CallbackQuery):
    await call.message.answer(" Burger // Narxi 1.5$ <a href='https://telegra.ph/file/eb6a17566c29ea0d3a887.jpg'> </a> .")
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text="ENG")
async def burger(call: types.CallbackQuery):
    await call.message.answer("Quyidagi til mavjud emas.\n Iltimos Uzbek tilini tanlang",reply_markup=tugmain)
    await call.message.delete()
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="RUS")
async def burger(call: types.CallbackQuery):
    await call.message.answer("Quyidagi til mavjud emas.\n Iltimos Uzbek tilini tanlang",reply_markup=tugmain)
    await call.message.delete()
    await call.answer(cache_time=60)


if __name__ =="__main__":
    executor.start_polling(dp, skip_updates=True)