import sqlite3
from sqlite3 import Error


class Database:
    DB = f'database/ardbot.db'  # путь к файлу

    def __init__(self):
        self.connection = sqlite3.connect(Database.DB)
        self.cur = self.connection.cursor()

    def __enter__(self):
        return self

    def __exit__(self, ext_type, exc_value, traceback):
        if isinstance(exc_value, Exception):
            self.connection.rollback()
            return "Error"
        else:
            pass
            # self.connection.commit()
        self.cur.close()
        self.connection.close()

    def close(self):
        self.connection.close()

    def execute(self, sql, val=''):
        self.cur.execute(sql, val)
        return "OK"

    def executemany(self, sql, val=''):
        self.cur.executemany(sql, val)
        return self.cur.fetchone()

    def commit(self):
        self.connection.commit()


##########################
"Пользовательские функции"


def request_balance(user_id):
    """ Запрос баланса пользователя """
    try:
        sql = "SELECT balance FROM Users WHERE id = :user_id"
        val = {'user_id': user_id}
        with Database() as db:
            db.cur.execute(sql, val)
            data = db.cur.fetchone()
            return data[0]

    except Error as e:
        msg = f'Ошибка: {e}'
        return msg


def add_balance(user_id, amount):

    sql = """UPDATE Users SET balance = balance + :amount WHERE id = :user_id;"""
    val = {'amount': amount, 'user_id': user_id}
    with Database() as db:
        try:
            data = db.execute(sql, val)
            db.commit()
            msg = f"{data}. Баланс пополнен на {amount} монет"
            return msg
        except Error as e:
            msg = f'Ошибка: {e}'
            return msg