from aiogram import Router, Bot, types
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command, CommandStart, Text

from ..keyboards.inline.keyboard import create_inline_kb, create_inline_kb_inside
from ..lexicon.lexicon import LEXICON_RU, LEXICON_HI_RU, LEXICON_CONTACTS, LEXICON_SRC_COMMANDS_RU, LEXICON_SRC_RU, \
    LEXICON_TEST_COMMANDS_RU, LEXICON_LIST_BUTTONS_CONTACTS, LEXICON_COMMANDS_RU, LEXICON_FAQ
from ..config_data.config import Config, load_config
import tg_botapp.telegram.config_bd.bd as bd
from ..utiles.service import msg_to_delete

# Инициализируем роутер уровня модуля
router: Router = Router()
keyboard = create_inline_kb(2, **LEXICON_COMMANDS_RU)
keyboard_contacts = create_inline_kb(1, **LEXICON_LIST_BUTTONS_CONTACTS)
keyboard_inside = create_inline_kb_inside(1, **LEXICON_TEST_COMMANDS_RU)


# Этот хэндлер срабатывает на команду /start
@router.message(CommandStart())
async def process_start_command(message: Message):
    print(message.json(indent=4, exclude_none=True))
    await message.answer(text=LEXICON_RU['/start'], reply_markup=keyboard)


# Этот хэндлер срабатывает на команду /help
@router.message(Command(commands='help'))
async def process_help_command(message: Message):
    print(message.from_user.id)
    await message.answer(text=LEXICON_RU['/help'], reply_markup=keyboard_inside)


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
    print('Правила')
    # keyboard = create_inline_kb(2, '/help', '/info', '/contacts', '/support')
    await message.answer(text=LEXICON_HI_RU['/rules'])


# Этот хэндлер срабатывает на команду /faq
@router.message(Command(commands='faq'))
async def process_faq_command(message: Message):
    await message.answer(text=LEXICON_FAQ['/faq'])


# Этот хэндлер срабатывает на команду /contacts
@router.message(Command(commands='contacts'))
async def process_help_command(message: Message):
    await message.answer(text=LEXICON_HI_RU['/contacts'])


# Этот хэндлер срабатывает на команду /contacts_admins
@router.message(Command(commands='contacts_admins'))
async def process_contacts_command(message: Message):
    await message.answer(text=LEXICON_CONTACTS['/contacts_admins'])


# Этот хэндлер срабатывает на команду /contacts_government
@router.message(Command(commands='contacts_government'))
async def process_contacts_command(message: Message):
    await message.answer(text=LEXICON_CONTACTS['/contacts_government'])


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
                    msg = await message.answer(text=f'С возвращением {name}!')
                    await msg_to_delete(msg)
                else:
                    bd.insert(user_id, member.username, name, False)
                    msg = await message.answer(
                        text=f'Доброго времени суток {name}! {LEXICON_HI_RU["hi"]}')
                    await msg_to_delete(msg)
        else:
            if message.from_user.id not in list_x:
                list_x.append(message.from_user.id)
            print(list_x)
            print(message.from_user.id)
        #     print(f'{str(message.chat.id)} ---> {message.chat.title} ---> ---> {message.from_user.first_name} -> {message.text}')
        #     print(message.message_thread_id)
    except TypeError:
        await message.reply(text=LEXICON_RU['no_echo'])


# # Обработчик нажатия на кнопку Помощь
# @router.callback_query(Text(text=['/help']))
# async def buttons_press_help(callback: CallbackQuery):
#     print('Это обработчик помощи')
#     await callback.answer(text=LEXICON_SRC_RU['/help'])


# Обработчик нажатия на кнопку Информация
@router.callback_query(Text(text=['/info']))
async def buttons_press_info(callback: CallbackQuery):
    print('Это обработчик инфо')
    if callback.message.text != 'info':
        await callback.message.edit_text(
            text=LEXICON_HI_RU['/info'],
            reply_markup=callback.message.reply_markup
        )
    await callback.answer(text='Давайте знакомиться')


# Обработчик нажатия на кнопку Правила
@router.callback_query(Text(text=['/rules']))
async def buttons_press_rules(callback: CallbackQuery):
    print('Это обработчик правил')
    if callback.message.text != 'rules':
        await callback.message.edit_text(
            text=LEXICON_HI_RU['/rules'],
            reply_markup=callback.message.reply_markup
        )
    await callback.answer(text='Правила чата')


# Обработчик нажатия на кнопку FAQ
@router.callback_query(Text(text=['/faq']))
async def buttons_press_faq(callback: CallbackQuery):
    print('Это обработчик FAQ')
    if callback.message.text != 'faq':
        await callback.message.edit_text(
            text=LEXICON_FAQ['/faq'],
            reply_markup=callback.message.reply_markup
        )
    await callback.answer(text='Ознакомьтесь с наиболее частыми вопросами')


# list_test = LEXICON_LIST_BUTTONS_CONTACTS

# Обработчик нажатия на кнопку Контакты
@router.callback_query(Text(text=['/contacts']))
async def buttons_press_contacts(callback: CallbackQuery):
    # keyb = create_inline_kb(2, *list_test)
    if callback.message.text != LEXICON_HI_RU['/contacts']:
        await callback.message.edit_text(
            text=LEXICON_HI_RU['/contacts'],
            reply_markup=keyboard_contacts)
    await callback.answer(text='Вы перешли в записную книжку')


# Обработчик нажатия на кнопку Админы
@router.callback_query(Text(text=['/contacts_admins']))
async def buttons_press_support(callback: CallbackQuery):
    print('Это обработчик Админов')
    if callback.message.text != 'contacts_admins':
        await callback.message.edit_text(
            text=LEXICON_CONTACTS['/contacts_admins'],
            reply_markup=callback.message.reply_markup
        )
    await callback.answer(text='Администраторы')


# Обработчик нажатия на кнопку Госорганы
@router.callback_query(Text(text=['/contacts_government']))
async def buttons_press_support(callback: CallbackQuery):
    print('Это обработчик Госорганов')
    if callback.message.text != 'contacts_government':
        await callback.message.edit_text(
            text=LEXICON_CONTACTS['/contacts_government'],
            reply_markup=callback.message.reply_markup
        )
    await callback.answer(text='Государственные органы')


# Обработчик нажатия на кнопку Поиск/госпитали
@router.callback_query(Text(text=['/contacts_hospitals']))
async def buttons_press_support(callback: CallbackQuery):
    print('Это обработчик Поиска/госпиталей')
    if callback.message.text != 'contacts_hospitals':
        await callback.message.edit_text(
            text=LEXICON_CONTACTS['/contacts_hospitals'],
            reply_markup=callback.message.reply_markup
        )
    await callback.answer(text='Больницы')


# Обработчик нажатия на кнопку Прошивка дронов
@router.callback_query(Text(text=['/contacts_drons_software']))
async def buttons_press_support(callback: CallbackQuery):
    print('Это обработчик Поиска/госпиталей')
    if callback.message.text != 'contacts_drons_software':
        await callback.message.answer(
            text=LEXICON_CONTACTS['/contacts_drons_software'],
            reply_markup=callback.message.reply_markup
        )
    await callback.answer(text='Прошивка дронов')


# Обработчик нажатия на кнопку Поддержка
@router.callback_query(Text(text=['/support']))
async def buttons_press_support(callback: CallbackQuery):
    print('Это обработчик поддержки')
    if callback.message.text != 'support':
        await callback.message.edit_text(
            text=LEXICON_HI_RU['/support'],
            reply_markup=callback.message.reply_markup
        )
    await callback.answer(text=LEXICON_HI_RU['/support'])


# Обработчик нажатия на кнопку Выход
@router.callback_query(Text(text=['/cancel']))
async def buttons_press(callback: CallbackQuery):
    print('Это обработчик возврата в начало')
    if callback.message.text != 'cancel':
        await callback.message.edit_text(
            text=LEXICON_RU['/start'],
            reply_markup=keyboard)
    await callback.answer(text='Вы находитесь в главном меню')
