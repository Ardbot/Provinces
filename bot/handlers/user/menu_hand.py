""" Основное меню """

from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text

from bot.database.db_sqlalchemy import registration_user, delete_user
from bot.markups import reply_markups
from bot.markups.languages.ru import start_msg


async def cmd_start(message: types.Message):
    """ Старт """
    await message.answer(f'Привет, {message.from_user.full_name}. {start_msg}')
    user_id = message.from_user.id
    username = message.from_user.full_name
    date = registration_user(user_id, username)
    await message.answer(date, reply_markup=reply_markups.menu)


async def lk_hand(message: types.Message):
    """ Вход в личный кабинет """
    await message.answer(f"Личный кабинет: {message.from_user.full_name}", reply_markup=reply_markups.lk)



async def work_hand(message: types.Message):
    """ Вход в категорию 'Работа' """
    await message.answer(f"Работа. Доступно {'...'} заданий")


async def cmd_cancel(message: types.Message, state: FSMContext):
    """ Отмена состояния машины и возврат в главное меню """
    await state.finish()
    await message.answer("Действие отменено", reply_markup=reply_markups.menu)

async def cmd_help_me(message: types.Message):
    """ Помощь """
    await message.answer("Чем помочь?\n"
                         "Пользовательское соглашение\n"
                         "Группа бота: @ExchangeYT")


def register_handlers_menu(dp: Dispatcher):
    dp.register_message_handler(cmd_start, commands="start", state="*")
    # dp.register_message_handler(cmd_start, state=RegForm.agreement)

    dp.register_message_handler(cmd_cancel, commands="cancel", state="*")
    dp.register_message_handler(cmd_cancel, Text(equals="Отмена", ignore_case=True), state="*")

    dp.register_message_handler(lk_hand, commands="lk", state="*")
    dp.register_message_handler(lk_hand, Text(equals="Личный кабинет", ignore_case=True), state="*")

    dp.register_message_handler(work_hand, commands="work")
    dp.register_message_handler(work_hand, Text(equals="Работа", ignore_case=True))

    dp.register_message_handler(cmd_help_me, commands="help", state="*")

    dp.register_message_handler(cmd_help_me, Text(equals="Помощь", ignore_case=True))






    # dp.register_message_handler(payment, commands="payment", state="*")