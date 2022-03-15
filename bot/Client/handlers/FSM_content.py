from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State


class ServiceForm(StatesGroup):
    """ ����������� ��������� """
    start = State()  # ���� � ����� ������ ���������
    # description_service = State()  # �������� ������
    # title_service = State()  #


async def FSM_start(message: types.Message):
    await message.answer("������� ��������:")
    await ServiceForm.start.set()
# id
# ��������
# �������
# ��������
# ���������


async def key_value(message: types.Message, state: FSMContext):
    """ ���������� ����� � �������� """
    await message.answer("������� ��������:")


async def save(message: types.Message, state: FSMContext):
    """ ���������� """



def register_handlers_commands(dp: Dispatcher):
    dp.register_message_handler(FSM_start, commands="FSM_start", state="*")
    dp.register_message_handler(key_value, commands="key_value", state="FSM_start")
    dp.register_message_handler(save, commands="save", state="FSM_start")

# ����������� ������. � ��� ���� � ��������. � ������ �������������� ������� ������ ������. �������� ���� � �������� ��������