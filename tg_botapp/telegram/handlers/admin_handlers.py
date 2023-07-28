from aiogram import Router, types, Bot
from aiogram.filters import Command, Text
from aiogram.types import Message, CallbackQuery
import tg_botapp.telegram.config_bd.bd as bd
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
ADMIN_LIST = [2222222, 111111111, 333333333]  # Свои значения id пользователей
ADMIN_ID = 222222    # id админа


async def send_sos_message(admin_id, recipient_id):
    message_all = 'Общий сбор'
    try:
        await Bot.send_message(recipient_id, message_all)
        await Bot.send_message(admin_id, f'SOS-сообщение отправлено пользователю с ID {recipient_id}')
    except Exception as e:
        print(f'Error sending message: {e}')


@IsAdmin
@router.message(Command(commands='sos'))
async def process_help_command(message: Message):
    print("Received /sos command")
    await message.answer(text=LEXICON_SOS_RU['/sos'], reply_markup=keyboard)


@IsAdmin
@router.callback_query(lambda callback: callback.data == 'sos')
async def admin_button_handler(callback: CallbackQuery):
    recipient_id = [admin for admin in ADMIN_LIST]
    for admin_id in ADMIN_LIST:
        print(f"Sending SOS message from admin {admin_id} to recipient {recipient_id}")
        await send_sos_message(admin_id, recipient_id)
    await callback.answer(text='Срочный вызов')
