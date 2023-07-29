from aiogram import Router, Bot
from aiogram.filters import Command, Text
from aiogram.types import Message, CallbackQuery

from tg_botapp.telegram.ZOV_src.lexicon_src import LEXICON_SOS_RU
from tg_botapp.telegram.config_data.config import Config, load_config
from tg_botapp.telegram.filters.filters import IsAdmin
from tg_botapp.telegram.keyboards.inline.keyboard import create_inline_kb, create_inline_kb_inside
from tg_botapp.telegram.lexicon.lexicon import LEXICON_TEST_COMMANDS_RU, LEXICON_LIST_BUTTONS_CONTACTS, \
    LEXICON_COMMANDS_RU

config: Config = load_config()

router: Router = Router()
keyboard = create_inline_kb(2, **LEXICON_COMMANDS_RU)
keyboard_contacts = create_inline_kb(1, **LEXICON_LIST_BUTTONS_CONTACTS)
keyboard_inside = create_inline_kb_inside(1, **LEXICON_TEST_COMMANDS_RU)


ADMIN_LIST = [415521486, 825886126, 333333333]  # Свои значения id пользователей
ADMIN_ID = 415521486  # id админа
bot = Bot(token='YOUR_TOKEN')


async def send_sos_message(admin_id, recipient_id):
    message = 'Общий сбор'
    for recipient_id in ADMIN_LIST:
        await bot.send_message(recipient_id, message)
        await bot.send_message(admin_id, f"Отправлен срочный вызов от админа с id{admin_id} пользователю\
         с id {recipient_id}")


@IsAdmin
@router.message(Command(commands='sos'))
async def process_help_command(message: Message):
    print("Received /sos command")
    await message.answer(text=LEXICON_SOS_RU['/sos'], reply_markup=keyboard)


@IsAdmin
@router.callback_query(Text(text=['/sos']))
async def buttons_press_faq(callback: CallbackQuery):
    print('Это обработчик SOS')
    recipient_id = [admin for admin in ADMIN_LIST]
    for admin_id in ADMIN_LIST:
        await send_sos_message(admin_id, recipient_id)
