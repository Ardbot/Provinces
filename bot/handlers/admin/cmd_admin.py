from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import IDFilter

from bot.config import ADMIN_ID
from bot.database.sql_db import add_balance, request_balance

admin_id = ADMIN_ID


def test(message: types.Message):
    print(add_balance(1, 5))
    print(request_balance(1))



def register_handlers_admin(dp: Dispatcher):
    pass
    # dp.register_message_handler(cmd_delete_user, commands="delete_user")  # , IDFilter(user_id=admin_id)
    dp.register_message_handler(test, IDFilter(user_id=admin_id), commands="test")
    # dp.register_message_handler(create_table, IDFilter(user_id=admin_id), commands="create_table")
    #
    # dp.register_message_handler(delete_user, commands="test", state="*")
