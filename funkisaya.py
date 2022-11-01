from email import message
from email.message import Message
import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import KeyboardButton,InlineKeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove, InlineKeyboardMarkup

API_TOKEN = '5350705889:AAE6KIK0McxXO92rxD0KdDjbYGmZCV6h0o4'
logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
@dp.callback_query_handler(text="Samsung")
async def asdd(call: types.CallbackQuery):
    await call.message.answer("Quyidagi bo'limlardan birini tanlang:")
    await call.message.delete()
    await call.answer(cache_time=60)