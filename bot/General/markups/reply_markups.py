from aiogram.types import ReplyKeyboardMarkup

""" Основное меню """

menu = ReplyKeyboardMarkup(resize_keyboard=True).add("Личный кабинет", "Команды")
menu.add("Помощь")

cancel = "Отмена"

help_me = ReplyKeyboardMarkup(resize_keyboard=True).add("О боте", "Команды")
help_me.add(cancel)


navigation = ReplyKeyboardMarkup(resize_keyboard=True)
navigation.add("Предыдущий", "Следующий")
navigation.add("Рандом", cancel)

""" Личный кабинет """

lk = ReplyKeyboardMarkup(resize_keyboard=True).add("Баланс", "Мои задания")
lk.add("Статистика канала", "Настройки")
lk.add(cancel)

agreement = ReplyKeyboardMarkup(resize_keyboard=True).add("Согласен", "Не согласен")

""" Баланс """
balance = ReplyKeyboardMarkup(resize_keyboard=True).add("Пополнить баланс", "Мои транзакции")
balance.add(cancel)

""" Настройки """
settings = ReplyKeyboardMarkup(resize_keyboard=True).add("Редактировать id канала", "Редактировать имя")
settings.add(cancel)

""" Работа """

work = ReplyKeyboardMarkup(resize_keyboard=True).add("Лайкать", "Смотреть")
work.add("Комментировать", "Подписаться")
work.add(cancel)

""" Задачи """

my_task = ReplyKeyboardMarkup(resize_keyboard=True).add("+Подписка", "+Комментарий")
my_task.add("+Лайк", "+Просмотр")
my_task.add(cancel)

pay = ReplyKeyboardMarkup(resize_keyboard=True).add("Оплатить")
pay.add(cancel)



# FSM = ReplyKeyboardMarkup(resize_keyboard=True).add("Оплатить", "Отмена")
# pay = ReplyKeyboardMarkup(resize_keyboard=True).add("Оплатить", "Отмена")



