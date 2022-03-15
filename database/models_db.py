from sqlalchemy import Column, ForeignKey, Integer, String, CheckConstraint
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

""" Создание базы данных """
engine = create_engine("sqlite:///database/provinces.db")  # , echo=True)
Base = declarative_base()


class User(Base):
    __tablename__ = 'Users'

    id = Column(Integer,  primary_key=True)
    nickname = Column(String(50), unique=True)

    user_name = Column(String(50), nullable=False, default="noname")
    patronymic = Column(String(50))
    surname = Column(String(50))
    balance = Column(Integer, CheckConstraint('balance >= 0'), default=0)
    email_user = Column(String(100))
    tg_id = Column(Integer)  # id телеграма
    phone_number = Column(String(250))
    location_oktmo = Column(Integer, default=45000000)  # Москва
    description = Column(String(500))
    rating = Column(Integer, default=0)


class Town(Base):
    """ Создает экземпляры городов """
    __abstract__ = True

    oktmo = Column(Integer, default=0, primary_key=True)
    name = Column(String(100), nullable=False)


class Product(Base):
    """ Товары """
    __tablename__ = 'Products'

    id_product = Column(Integer, primary_key=True)
    name_product = Column(String(250))
    description = Column(String(500))
    price = Column(Integer)
    count = Column(Integer)
    category = Column(Integer)
    seller = Column(Integer, ForeignKey("Users.id"))

class Service(Base):
    """ Услуги """
    __tablename__ = 'Services'

    id_service = Column(Integer, primary_key=True)
    name_service = Column(String(250))
    description = Column(String(500))
    price = Column(Integer)
    seller = Column(Integer, ForeignKey("Users.id"))  # Владелец


class RealEstate(Base):
    """ Недвижимость """
    __tablename__ = 'RealEstate'

    id_real_estate = Column(Integer, primary_key=True)
    name_real_estate = Column(String(250))
    address = Column(String(250))
    inn = Column(Integer)
    working_hours = Column(String(500))
    category = Column(String(250))
    seller = Column(Integer, ForeignKey("Users.id"), default=1)    # Владелец



# class Gorod(Town):
#     data = Postindex('679000')
#     __tablename__ = data['Index']

Base.metadata.create_all(engine)
