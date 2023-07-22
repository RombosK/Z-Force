import tg_botapp.telegram.config_bd.bd as bd
from aiogram import Bot, Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from tg_botapp.telegram.config_data.config import Config, load_config
from tg_botapp.telegram.lexicon.lexicon import (LEXICON_CONTACTS,
                                                LEXICON_HI_RU,
                                                LEXICON_RU)

config: Config = load_config()

# Инициализируем роутер уровня модуля
router: Router = Router()


# Этот хэндлер срабатывает на команду /start
@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text=LEXICON_RU['/start'])


# Этот хэндлер срабатывает на команду /help
@router.message(Command(commands='help'))
async def process_help_command(message: Message):
    await message.answer(text=LEXICON_RU['/help'])


# Этот хэндлер срабатывает на команду /info
@router.message(Command(commands='info'))
async def process_help_command(message: Message):
    await message.answer(text=LEXICON_HI_RU['/info'])


# Этот хэндлер срабатывает на команду /support
@router.message(Command(commands='support'))
async def process_help_command(message: Message):
    await message.answer(text=LEXICON_HI_RU['/support'])


# Этот хэндлер срабатывает на команду /rules
@router.message(Command(commands='rules'))
async def process_help_command(message: Message):
    await message.answer(text=LEXICON_HI_RU['/rules'])


# Этот хэндлер срабатывает на команду /contacts
@router.message(Command(commands='contacts'))
async def process_help_command(message: Message):
    await message.answer(text=LEXICON_HI_RU['/contacts'])


# Этот хэндлер срабатывает на команду /contacts_goverment
@router.message(Command(commands='contacts_goverment'))
async def process_contacts_command(message: Message):
    await message.answer(text=LEXICON_CONTACTS['/contacts_goverment'])


# Этот хэндлер срабатывает на команду /contacts_hospitals
@router.message(Command(commands='contacts_hospitals'))
async def process_contacts_command(message: Message):
    await message.answer(text=LEXICON_CONTACTS['/contacts_hospitals'])


@router.message()
async def send_echo(message: Message, bot: Bot):
    try:
        """Проверяем есть ли пользователь в базе"""
        if message.new_chat_members != None:
            for member in message.new_chat_members:
                user_id = member.id
                name = member.first_name
                if bd.select(user_id):
                    await message.answer(text=f'С возвращением {name}!')
                else:
                    bd.insert(user_id, member.username, name, False)
                    await message.answer(
                        text=f'Доброго времени суток {name}! {LEXICON_HI_RU["hi"]}')
        # else:
        #     print(f'{str(message.chat.id)} ---> {message.chat.title} ---> ---> {message.from_user.first_name} -> {message.text}')
        #     print(message.message_thread_id)
    except TypeError:
        await message.reply(text=LEXICON_RU['no_echo'])
