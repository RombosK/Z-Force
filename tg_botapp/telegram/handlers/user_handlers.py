from aiogram import Router, Bot
from aiogram.types import Message, ChatPermissions, Update

from tg_botapp.telegram.lexicon.lexicon import LEXICON_RU
import tg_botapp.telegram.config_bd.bd as bd

# Инициализируем роутер уровня модуля
router: Router = Router()


# Этот хэндлер будет срабатывать на любые ваши сообщения,
# кроме команд "/start" и "/help"
@router.message()
async def send_echo(message: Message, bot: Bot):
    try:
        """Проверяем есть ли пользователь в базе"""
        if message.new_chat_members != None:
            for member in message.new_chat_members:
                print(member)
                user_id = member.id
                name = member.first_name
                if bd.select(user_id):
                    await message.answer(text=f'С возвращением ')
                else:
                    bd.insert(user_id, member.username, name, False)
                    await message.answer(
                        text=f'Приветствуем Вас {name}! Мы рады что Вы присоединились к нашему волонтерскому движению!')
                    await bot.send_message(user_id, 'Я бот! Если у Вас есть вопросы, пишите мне!')
        # await message.answer(text=LEXICON_RU['other_answer'])
        # """Далее робот выставляет ограничения!"""
        # new_permissions = ChatPermissions(
        #     can_send_messages=False
        # )
        # await bot.set_chat_permissions(message.chat.id, new_permissions)
        # """Закончил выставлять ограничения!"""
        # """Удаление сообщения"""
        # await bot.delete_message(message_id=message.message_id, chat_id=message.chat.id)
    except TypeError:
        await message.reply(text=LEXICON_RU['no_echo'])