from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State


class ServiceForm(StatesGroup):
    """ Конструктор контекста """
    start = State()  # Вход в режим Машины состояний
    # description_service = State()  # Описание услуги
    # title_service = State()  #


async def FSM_start(message: types.Message):
    await message.answer("Введите название:")
    await ServiceForm.start.set()
# id
# Название
# Атрибут
# значение
# Сохранить


async def key_value(message: types.Message, state: FSMContext):
    """ Добавление ключа и значения """
    await message.answer("Введите название:")


async def save(message: types.Message, state: FSMContext):
    """ Сохранение """



def register_handlers_commands(dp: Dispatcher):
    dp.register_message_handler(FSM_start, commands="FSM_start", state="*")
    dp.register_message_handler(key_value, commands="key_value", state="FSM_start")
    dp.register_message_handler(save, commands="save", state="FSM_start")

# формируется строка. В ней ключ и значение. В режиме редактирования выдаеся список ключей. Выбираем ключ и изменяем значение