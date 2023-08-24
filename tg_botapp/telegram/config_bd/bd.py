import datetime
import sqlite3

import os

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
django.setup()

# from aiogram.types import CallbackQuery, Message
# from authapp.models import User
# from django.contrib import auth
# from aiogram import Bot

conn = sqlite3.connect('db.sqlite3')
cur = conn.cursor()


cur.execute("""CREATE TABLE IF NOT EXISTS users(
   userid INT PRIMARY KEY,
   username TEXT,
   name TEXT,
   admin BOOL);
""")
conn.commit()


def insert(user_id: int, user_name: str, name: str, admin: bool):
    cur.execute('INSERT INTO users (userid, username, name, admin) VALUES (?, ?, ?, ?)',
                (user_id, user_name, name, admin))

    conn.commit()


def select(telegram_id):
    result = cur.execute('SELECT * FROM users WHERE id = ?', (id,))
    for i in result:
        return len(i) > 0


# if __name__ == '__main__':
# 	insert_mes(725455605, 111, datetime.time)


