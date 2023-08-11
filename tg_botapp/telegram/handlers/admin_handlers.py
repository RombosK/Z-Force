from aiogram import Router, Bot
from aiogram.filters import Command, Text
from aiogram.types import Message, CallbackQuery
from ..ZOV_src.lexicon_src import LEXICON_SOS_RU
from ..config_data.config import Config, load_config
from ..filters.filters import IsAdmin
from ..keyboards.inline.keyboard import create_inline_kb, create_inline_kb_inside, admin_menu
from ..lexicon.lexicon import LEXICON_TEST_COMMANDS_RU, LEXICON_LIST_BUTTONS_CONTACTS, LEXICON_RU

config: Config = load_config()

router: Router = Router()
router.message.filter(IsAdmin(config.tg_bot.admin_ids))
keyboard = admin_menu
keyboard_contacts = create_inline_kb(1, **LEXICON_LIST_BUTTONS_CONTACTS)
keyboard_inside = create_inline_kb_inside(1, **LEXICON_TEST_COMMANDS_RU)


#
# async def send_sos_message(admin_id, recipient_id):
#     message = 'Общий сбор'
#     for recipient_id in config.tg_bot.admin_ids:
#         await bot.send_message(recipient_id, message)
#         await bot.send_message(admin_id, f"Отправлен срочный вызов от админа с id{admin_id} пользователю\
#          с id {recipient_id}")


@router.message(Text(text='🆘 HELP'))
async def process_help_command1(message: Message, bot: Bot):
    print('Это обработчик SOS')
    print(message.from_user)
    for admin_id in config.tg_bot.admin_ids:
        print(admin_id)
        await bot.send_message(admin_id,
                               str(f'{message.from_user.first_name}(@{message.from_user.username}) просит о помощи!'),
                               reply_markup=keyboard)


# Этот хэндлер срабатывает на команду /help
@router.message(Command(commands='help'))
async def process_help_command(message: Message):
    print(message.from_user.id)
    await message.answer(text=LEXICON_RU['/sos'], reply_markup=keyboard_inside)


@router.message()
async def process_help_command(message: Message, bot: Bot):
    print("Received /sos command")
    await bot.send_message(message.from_user.id, LEXICON_SOS_RU['/sos'], reply_markup=keyboard)
    # await message.answer(text=LEXICON_SOS_RU['/sos'], reply_markup=keyboard)


