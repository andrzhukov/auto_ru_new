import asyncio
import logging

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils.executor import start_webhook
from keyboards import main_kb, car_kb

API_TOKEN = '5206470113:AAFmrSKFiTOk9GnsQ69cw8YtXIz5cIZuO50'

# webhook settings
WEBHOOK_HOST = 'https://your.domain'
WEBHOOK_PATH = ''
WEBHOOK_URL = 'https://09a3-217-74-47-7.eu.ngrok.io'

# webserver settings
WEBAPP_HOST = '127.0.0.1'  # or ip
WEBAPP_PORT = 5001

logging.basicConfig(level=logging.INFO)

loop = asyncio.get_event_loop()
bot = Bot(token=API_TOKEN, loop=loop)
dp = Dispatcher(bot)

'''***************** КЛИЕНТСКАЯ ЧАСТЬ ********************'''

@dp.message_handler(commands = ['start'])
async def command_start(message : types.Message):
    print(message)
    await bot.send_message(message.chat.id, 'Привет, ' + message.chat.first_name + '!\n'\
                           'Бот поможет тебе моментально узнавать о новых объявлениях о продаже авто на сайтах auto.ru, avito.ru.\n\n'\
                           'Далее можно посмотреть общую информацию о боте или сразу перейти к настройке параметров поиска', reply_markup=main_kb)

@dp.message_handler(text = 'Добавить новые параметры поиска')
async def command_start(message : types.Message):
    print(message)
    await bot.send_message(message.chat.id, 'Настроим параметры поиска.\n\n'\
                           'Выбери марку автомобиля.', reply_markup=car_kb)

@dp.message_handler()
async def echo(message: types.Message):
    print(message)
    await bot.send_message(message.chat.id, message.text)



async def on_startup(dp):
    await bot.set_webhook(WEBHOOK_URL)
    # insert code here to run it after start


async def on_shutdown(dp):
    # insert code here to run it before shutdown
    pass


if __name__ == '__main__':
    start_webhook(dispatcher=dp, webhook_path=WEBHOOK_PATH, on_startup=on_startup, on_shutdown=on_shutdown,
                  skip_updates=True, host=WEBAPP_HOST, port=WEBAPP_PORT)