from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import IDFilter

from bot.Admin.config import ADMIN_ID

admin_id = ADMIN_ID

def register_handlers_admin(dp: Dispatcher):
    pass
    # dp.register_message_handler(cmd_delete_user, commands="delete_user")  # , IDFilter(user_id=admin_id)
    # dp.register_message_handler(test, IDFilter(user_id=admin_id), commands="test")
    # dp.register_message_handler(create_table, IDFilter(user_id=admin_id), commands="create_table")
    #
    # dp.register_message_handler(delete_user, commands="test", state="*")
