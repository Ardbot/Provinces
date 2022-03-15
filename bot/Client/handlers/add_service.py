""" Недвижимость. FSM """
from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text, state
from aiogram.dispatcher.filters.state import StatesGroup, State


class ServiceForm(StatesGroup):
    name_service = State()  # Имя услуги
    description_service = State()  # Описание услуги
    title_service = State()  #


async def service_start(message: types.Message):
    await message.answer("Введите название услуги:")
    await ServiceForm.name_service.set()


async def service_name(message: types.Message, state: FSMContext):
    """ Добавляем название услуги"""
    if len(message.text) >= 25:
        await message.answer("Не более 25 символов")
    elif message.text == "/add_service":
        await message.answer("Введите название услуги:")
    else:
        await state.update_data(name=message.text)
        await message.answer(f"Имя услуги:'{message.text}'")
        await ServiceForm.description_service.set()

async def service_description(message: types.Message, state: FSMContext):
    """ Добавляем описание """
    if len(message.text) >= 25:
        await message.answer("Не более 25 символов")
    elif message.text == "/add_service":
        await message.answer("Введите название услуги:")
    else:
        await state.update_data(name=message.text)
        await message.answer(f"Имя услуги:'{message.text}'")
        await ServiceForm.description_service.set()


def register_handlers_commands(dp: Dispatcher):
    dp.register_message_handler(service_start, commands="add_service", state="*")
    dp.register_message_handler(service_start, Text(equals="Добавить услугу", ignore_case=True))

    dp.register_message_handler(service_start, state="name_service")

