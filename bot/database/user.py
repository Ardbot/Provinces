from sqlite3 import Error

from bot.database.sql_db import Database

create_table_users = """CREATE TABLE Users (
    id             INTEGER       NOT NULL,
    nickname       VARCHAR (50),
    tg_id          INTEGER,
    user_name      VARCHAR (50)  NOT NULL,
    patronymic     VARCHAR (50),
    surname        VARCHAR (50),
    balance        INTEGER       CHECK (balance >= 0),
    email_user     VARCHAR (100),
    phone_number   VARCHAR (250),
    location_oktmo INTEGER,
    PRIMARY KEY (
        id
    ),
    UNIQUE (
        nickname
    )
);"""





