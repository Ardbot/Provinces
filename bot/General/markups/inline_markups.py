""" Кнопки под сообщением """
from aiogram import types


def inline_btn(text, id_channel2):
    url = "https://www.youtube.com/channel/" + id_channel2

    buttons = [
        types.InlineKeyboardButton(text=text, url=url),
        types.InlineKeyboardButton(text="Подписался", callback_data="work_subs_state"),
        # types.InlineKeyboardButton("Отмена")
    ]
    inline_keyboard = types.InlineKeyboardMarkup(row_width=3).add(*buttons)
    return inline_keyboard



# def inline_btn(text, url):
#     buttons = types.InlineKeyboardButton(text=text, url=url)
#     inline_keyboard = types.InlineKeyboardMarkup(row_width=1).add(buttons)
#     return inline_keyboard