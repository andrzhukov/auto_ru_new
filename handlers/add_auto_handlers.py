from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types
from CarpostBot import bot
from keyboards import inl_kb

class FSMAutoAdd(StatesGroup):
    brand = State()
    model = State()
    year = State()
    engine_power = State()
    miliage = State()
    price = State()

# First dialog with button "Выбери марку автомобиля"
@dp.message_handler(text = 'Добавить новые параметры поиска', state=None)
async def command_start(message : types.Message):
    print(message)
    await bot.send_message(message.chat.id, 'Настроим параметры поиска.\n\n'\
                           'Выбери марку автомобиля.', reply_markup=inl_kb)
