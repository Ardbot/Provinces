""" Недвижимость. FSM """
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State


class RealtyForm(StatesGroup):
    name = State()  # Название организации
    count_sub = State()  # Кол-во накрученных подписчиков
    payment_sub = State()  # Счет на оплату


async def realty_start(message: types.Message):
    await message.answer("➕ Добавить организацию\n"
                         "Введите название объекта:")
    await RealtyForm.name.set()


async def realty_name(message: types.Message, state: FSMContext):
    # price = int(message.text)
    # a = input_date.input_int(price, 5, 100)
    pass