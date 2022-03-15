#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Общиие команды для бота"""

from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text

from bot.General.markups import reply_markups


async def cmd_start(message: types.Message, state: FSMContext):
    """ Стартовое сообщение """
    await state.finish()
    await message.answer("Добро пожаловать в провинцию!", reply_markup=reply_markups.menu)

async def cmd_help(message: types.Message):
    """ Помощь """
    await message.answer("Помощь", reply_markup=reply_markups.help_me)


async def cmd_cancel(message: types.Message, state: FSMContext):
    """ Отмена состояния машины и возврат в главное меню """
    await state.finish()
    await message.answer("Действие отменено", reply_markup=reply_markups.menu)


async def other(message: types.Message):
    await message.answer("Я не знаю что это!")
    # Но хочу помочь

def register_handlers_general_commands(dp: Dispatcher):
    """ Хендлеры. Общии команды для функций """
    dp.register_message_handler(cmd_start, commands="start", state="*")
    dp.register_message_handler(cmd_cancel, commands="cancel", state="*")
    dp.register_message_handler(cmd_cancel, Text(equals="Отмена", ignore_case=True))
    dp.register_message_handler(cmd_help, commands="help", state="*")
    dp.register_message_handler(cmd_help, Text(equals="Помощь", ignore_case=True))


def register_handlers_other(dp: Dispatcher):
    dp.register_message_handler(other)
