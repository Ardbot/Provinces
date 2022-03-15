import asyncio

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import BotCommand

# Регистрация команд, отображаемых в интерфейсе Telegram
from bot.Admin import config
from bot.Admin.create_bot import dp, bot
from bot.Admin.handlers.cmd_admin import register_handlers_admin
from bot.Client.handlers.add_service import register_handlers_commands

from bot.General.handlers.common import register_handlers_general_commands, register_handlers_other


async def set_commands(bot1: Bot):
    commands = [
        BotCommand(command="/add_service", description="тест функции"),
        BotCommand(command="/start", description="Старт и регистрация"),
        BotCommand(command="/lk", description="Личный кабинет"),
        BotCommand(command="/cancel", description="Отменить текущее действие")
    ]
    await bot1.set_my_commands(commands)


async def main():
    """ Главная функция """

    """ Регистрация модулей """

    """ Регистрация хэндлеров """
    register_handlers_general_commands(dp)
    register_handlers_admin(dp)
    register_handlers_commands(dp)
    register_handlers_other(dp)

    """ Установка команд бота """
    await set_commands(bot)

    """ Запуск поллинга """
    # await dp.skip_updates()  # пропуск накопившихся апдейтов (необязательно)
    await dp.start_polling()


if __name__ == '__main__':
    asyncio.run(main())
