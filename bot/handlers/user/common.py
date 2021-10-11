#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Общиие команды для бота"""

from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text


async def cmd_next_step(state: FSMContext):
    """ Производит в состоянии шаг вперед """
    # await RegForm.next()
    pass


async def other(message: types.Message):
    await message.answer("Я не знаю что это!")


""" Хендлеры. Регистрируют команды для функций """


def register_handlers_commands(dp: Dispatcher):
    dp.register_message_handler(cmd_next_step, commands="next", state="*")
    dp.register_message_handler(cmd_next_step, Text(equals="Следующий", ignore_case=True))

    dp.register_message_handler(cmd_next_step, commands="next", state="*")
    dp.register_message_handler(cmd_next_step, Text(equals="Следующий", ignore_case=True))
    # dp.register_message_handler(cmd_start, state=RegForm.agreement)


def register_handlers_other(dp: Dispatcher):
    dp.register_message_handler(other)
