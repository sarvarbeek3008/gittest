import logging
from urllib import response
import requests
from aiogram import Bot, Dispatcher, executor, types
# API_TOKEN = '5357775034:AAHYTTXm8890fKEf6k6cnS7R6OW8e8PugcY'
API_KEY = 'c976e0348ad4ab56b71760e4bb96eaa9'
from pprint import pprint as p
currency = 'USD'
url=f"https://v6.exchangerate-api.com/v6/{API_KEY}/pair/{currency}/UZS"

response = requests.get(url)
print(response.status_code)


logging.basicConfig(level=logging.INFO)


# bot = Bot(token=API_TOKEN)
# dp = Dispatcher(bot)

# @dp.message_handler(commands=['start', 'help'])
# async def send_welcome(message: types.Message):
  
#     await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")
# @dp.message_handler()
# async def echo(message: types.Message):
  
#     await message.answer(message.text)

# if __name__ == '__main__':
#     executor.start_polling(dp, skip_updates=True)