
from loguru import logger
from sqlalchemy import create_engine, exc
from sqlalchemy.orm import sessionmaker

from bot.database.models_db import User, engine

# Флаг echo включает ведение лога через стандартный модуль logging Питона.
# Когда он включен, мы увидим все созданные нами SQL-запросы.
session = sessionmaker(bind=engine)
s = session()

def registration_user(user_id, name):
    """ Регистрация пользователя """
    try:
        reg = User(tg_id=user_id, user_name=name)
        s.add(reg)
        s.commit()
        msg = f"Пользователь: {name} ({user_id}) зарегистрирован."
        logger.info(msg)
        return msg
    except exc.SQLAlchemyError as e:
        logger.error(f"Повторная попытка регистрации:{user_id} {e}")
        return f"Вы уже зарегистрированы ранее!"
    finally:
        s.close()


def delete_user(user_id):
    """ Удаление пользователя """
    try:
        q = s.query(User).filter_by(user_id=user_id).delete()
        # print(q)  # Выводит 1 если запись была найдена, 0 если не найдена
        if q == 1:
            s.commit()
            logger.info(f"Пользователь '{user_id}' удален.")
            return f"Пользователь '{user_id}' удален."
        elif q == 0:
            logger.error(f"Пользователь '{user_id}' не найден")
            return f"Пользователь '{user_id}' не найден"
        else:
            logger.error(f"Пользователь '{user_id}' не найден")
            return f"Ошибка удаления. id: {user_id}"
    except exc.SQLAlchemyError as e:
        logger.error(f"Ошибка удаления. id: {user_id}")
        return f"Ошибка удаления. id: {user_id}"
    finally:
        s.close()