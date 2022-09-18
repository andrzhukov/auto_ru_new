import asyncio
import logging
import os, hashlib

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils.executor import start_webhook
from keyboards import main_kb, car_kb
from aiogram.types import InputTextMessageContent, InlineQueryResultArticle
from aiogram.types import update
from search import Searcher

API_TOKEN = '5206470113:AAFmrSKFiTOk9GnsQ69cw8YtXIz5cIZuO50'

# webhook settings
WEBHOOK_HOST = 'https://your.domain'
WEBHOOK_PATH = ''
WEBHOOK_URL = 'https://27d0-62-217-188-253.eu.ngrok.io'

# webserver settings
WEBAPP_HOST = '127.0.0.1'  # or ip
WEBAPP_PORT = 5001

logging.basicConfig(level=logging.INFO)

loop = asyncio.get_event_loop()
bot = Bot(token=API_TOKEN, loop=loop)
dp = Dispatcher(bot)
#test brands for inline mode
brands = ['BMW', 'Mercedes', 'Land Rover', 'KIA', 'Mitsubishi', 'Hyundai', 'Toyota', 'Audi', 'Honda', 'Haval',
          'Geely', 'Chery', 'Suzuki', 'LADA', 'Ford', 'Opel', 'Chevrolet', 'Jaguar', 'Citroen', 'Peugeout', 'Daewoo', 'EXEED',
          'Infiniti', 'Acura', 'Lexus', 'Jeep', 'MINI', 'Mazda', 'Nissan', 'Porsche', 'Renault', 'Skoda']
search = Searcher(brands)

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

@dp.inline_handler()
# async def inline_handler(query: types.InlineQuery):
#     text = query.query or 'echo'
async def inline_handler(query: update.InlineQuery):
    query_new = query.query
    query_new = query_new.rstrip().lower()
    search_brands = search.parse_guery(text=query_new)
    articles = []
    for idx in range(0,len(search_brands)):
        articles.append(InlineQueryResultArticle(
            id = idx+1,
            title = search_brands[idx],
            input_message_content=InputTextMessageContent(
                message_text=search_brands[idx])))

    await query.answer(results=articles, cache_time=1, is_personal=True)


if __name__ == '__main__':
    start_webhook(dispatcher=dp, webhook_path=WEBHOOK_PATH, on_startup=on_startup, on_shutdown=on_shutdown,
                  skip_updates=True, host=WEBAPP_HOST, port=WEBAPP_PORT)