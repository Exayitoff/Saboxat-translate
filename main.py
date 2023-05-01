import requests

import logging

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '5816561695:AAHLelzJxrPTJhSmPs2XjqRFbhwsnEQn4nE'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    
    await message.reply("Assalomu aleykum ushbu bot 3 ta tilga tarjima qila oladi!")



@dp.message_handler()
async def echo(message: types.Message):
    xabar = message.text
    r = requests.get(f'https://trans.noxi8.repl.co/ru/text={xabar}')
    r2 = requests.get(f'https://trans.noxi8.repl.co/en/text={xabar}')
    r3 = requests.get(f'https://trans.noxi8.repl.co/ar/text={xabar}')
    r4 = requests.get(f'https://trans.noxi8.repl.co/fr/text={xabar}')
    r5 = requests.get(f'https://trans.noxi8.repl.co/da/text={xabar}')
    response3 = r3.json()['text']
    response4 = r4.json()['text']
    response5 = r5.json()['text']
    response2 = r2.json()['text']
    response = r.json()['text']
    await message.reply(f'rus tilidagi tarjimasi : {response}\nIngliz tilidagi tarjimasi : {response2}\nArab tilidagi tarjimasi : {response3}\nFransuz tilidagi tarjimasi : {response4}\nDanish tilidagi tarjimasi : {response5}')
    

   


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
