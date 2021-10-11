""" Личный кабинет. view """

from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text


async def my_balance_hand(message: types.Message):
    """ Меню: Мой баланс """
    # balance = await db_sql.request_balance(message.from_user.id)
    # balance = db_sqlalchemy.request_balance(message.from_user.id)
    # print(balance)
    #
    # await message.answer(f"Баланс: {balance} монет\n"
    #                      "/add_balance - Пополнить баланс\n"
    #                      "/my_transaction 5 - Мои транзакции. Кол-во - 5\n", reply_markup=reply_markups.balance)


async def my_transaction(message: types.Message):
    """ Транзакции пользователя """
    # count = message.get_args()  # аргумент функции. задает кол-во записей
    # if not count:
    #     transaction = await request_transaction(message.from_user.id)
    # else:
    #     if count.isdigit():
    #         transaction = await request_transaction(message.from_user.id, count)
    #     else:
    #         transaction = await request_transaction(message.from_user.id)
    # print(transaction)
    # data = '\n'.join(transaction)

    # await message.answer(f"Транзакция средств:\n{transaction}", reply_markup=reply_markups.balance)


async def add_balance_hand(message: types.Message):
    amount = 250
    # data = await add_balance(message.from_user.id, amount)
    # data = await add_balance(message.from_user.id, amount)

    await message.answer(amount)


# async def deduct_balance_hand(message: types.Message):


async def settings(message: types.Message):
    # await SetForm.setting.set()
    await message.answer("Выберете действие:\n"
                         "/edit_id_channel - Редактировать id канала\n"
                         "/edit_name - Редактировать имя")


def register_handlers_lk(dp: Dispatcher):

    dp.register_message_handler(my_balance_hand, commands="my_balance", state="*")
    dp.register_message_handler(my_balance_hand, Text(equals="Баланс", ignore_case=True), state="*")

    dp.register_message_handler(add_balance_hand, commands="add_balance", state="*")
    dp.register_message_handler(add_balance_hand, Text(equals="Пополнить баланс", ignore_case=True), state="*")

    dp.register_message_handler(my_transaction, commands="my_transaction", state="*")
    dp.register_message_handler(my_transaction, Text(equals="Мои транзакции", ignore_case=True), state="*")



    """ Настройки бота """
    dp.register_message_handler(settings, commands="settings", state="*")  # Доступна во всех местах
    dp.register_message_handler(settings, Text(equals="Настройки", ignore_case=True), state="*")

