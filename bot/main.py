import asyncio

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import BotCommand

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine


from bot import config
from bot.database import models_db

from bot.handlers.admin.cmd_admin import register_handlers_admin
from bot.handlers.user.menu_hand import register_handlers_menu
from bot.handlers.user.common import register_handlers_commands, register_handlers_other

from bot.handlers.user.lk_hand import register_handlers_lk


# Регистрация команд, отображаемых в интерфейсе Telegram
async def set_commands(bot: Bot):
    commands = [
        BotCommand(command="/delete_user", description="тест функции"),
        BotCommand(command="/start", description="Старт и регистрация"),
        BotCommand(command="/payment", description="Оплата"),
        BotCommand(command="/work", description="Работа"),
        BotCommand(command="/lk", description="Личный кабинет"),
        BotCommand(command="/cancel", description="Отменить текущее действие")
    ]
    await bot.set_my_commands(commands)


async def main():
    """ Объявление и инициализация объектов бота и диспетчера """
    bot = Bot(token=config.TOKEN)
    dp = Dispatcher(bot, storage=MemoryStorage())



    """ Регистрация модулей """

    """ Регистрация хэндлеров """
    register_handlers_commands(dp)
    register_handlers_admin(dp)
    register_handlers_menu(dp)
    register_handlers_lk(dp)


    register_handlers_other(dp)

    """ Установка команд бота """
    await set_commands(bot)

    """ Запуск поллинга """
    # await dp.skip_updates()  # пропуск накопившихся апдейтов (необязательно)
    await dp.start_polling()


if __name__ == '__main__':
    asyncio.run(main())
