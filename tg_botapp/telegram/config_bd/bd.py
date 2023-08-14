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


def select(id):
    result = cur.execute('SELECT * FROM users WHERE userid = ?', (id,))
    for i in result:
        return len(i) > 0


# if __name__ == '__main__':
# 	insert_mes(725455605, 111, datetime.time)


# class BotLogic:
#
#     def __init__(self, bot: Bot, telegram_id: int, telegram_username: str):
#         self.bot = bot
#         self.telegram_id = telegram_id
#         self.telegram_username = telegram_username
#
#     @staticmethod
#     async def _get_answer_from_conv(conv: Message, question: str):
#         """
#         Функция-обертка над фрагментом диалога
#         (отправит пользователю уведомление, есил время ожилания ответа истечет)
#         """
#
#         timeout_message = 'Время ответа истекло'
#         try:
#             await conv.answer(question)
#             answer = await conv.get_current()
#             return answer.text
#         except Exception as e:
#             await conv.answer(timeout_message)
#
#     @staticmethod
#     def _press_event(user_id: int) -> CallbackQuery:
#         """
#         Вспомогательная функция для отслеживания кнопки, нажатой в диалоге
#         """
#         return CallbackQuery(func=lambda e: e.sender_id == user_id)
#
#     @staticmethod
#     def _authorize(username: str, password: str) -> bool:
#         user = auth.authenticate(username=username, password=password)
#         if user:
#             return True
#         return False
#
#     async def _merge_accounts(self, callback: CallbackQuery, message: Message, bot: Bot) -> None:
#         """
#             Функция связывания аккаунтов:
#             - в случае успешной авторизации аккаунту в базе добавляется переданный telegram id
#             """
#
#         username = await self._get_answer_from_conv(conv=message, question='Введи имя пользователя')
#         if username:
#             password = await self._get_answer_from_conv(conv=message, question='Введи пароль')
#             if password:
#                 # Авторизация базовым аккаунтом системы
#                 authorized = self._authorize(username=username, password=password)
#
#                 if authorized:
#                     # Добавляем аккаунту telegram id
#                     current_user = User.objects.get(username=username)
#                     current_user.telegram_id = self.telegram_id
#                     current_user.save()
#                     await callback.answer(text=
#                                           'Аккаунты связаны: login {current_user.username}, \
#                                       telegram_id {current_user.telegram_id}')
#                 else:
#                     await callback.answer(text='Неверный логин или пароль')
#
#     async def _create_account(self, conv: Message) -> None:
#         """
#         Функция создания аккаунта в системе на основе telegram id
#         """
#
#         new_user = User(telegram_id=self.telegram_id, username=self.telegram_username)
#         new_user.save()
#         await conv.answer(f'Создан новый аккаунт: login {new_user.username}, telegram_id {new_user.telegram_id}')
#
#     async def send_welcome_back(self):
#         await self.bot.send_message(self.telegram_id, 'С возвращением!')
#
#     async def create_or_merge_account(self):
#         """
#         Функция создания нового аккаунта на базе telegram id
#         или связи telegram id с существующим аккаунтом
#         """
#
#         async with self.bot.send_message(self.telegram_id) as conv:
#             buttons = [Button.inline('Да, связать аккаунты', b'merge'),
#                        Button.inline('Нет, создать аккаунт', b'create')]
#             await conv.send_message('Аккаунт не найден. Ты уже регистрировался на сайте?', buttons=buttons)
#
#             try:
#                 press = await conv.wait_event(self._press_event(self.telegram_id))
#                 if press.data == b'merge':
#                     # связывание аккаунтов
#                     await self._merge_accounts(conv)
#                 elif press.data == b'create':
#                     # создание аккаунта
#                     await self._create_account(conv)
#             except Exception as e:
#                 pass
