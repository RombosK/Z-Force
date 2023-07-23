from aiogram import Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from aiogram.utils.keyboard import InlineKeyboardBuilder

from tg_botapp.telegram.lexicon.lexicon import LEXICON_COMMANDS_RU

dp: Dispatcher = Dispatcher()


# Функция генерит инлайн-клавиатуру автоматом в зависимости от ЛЕКСИКОНА
def create_inline_kb(width: int, *args: str, **kwargs: str) -> InlineKeyboardMarkup:
    # Инициализация билдера
    kb_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
    # Инициализация списка кнопок
    buttons: list[InlineKeyboardButton] = []

    # Заполнение списка кнопками из аргументов args и kwargs
    if args:
        for button in args:
            buttons.append(InlineKeyboardButton(
                text=LEXICON_COMMANDS_RU[button] if button in LEXICON_COMMANDS_RU else button,
                callback_data=button))
    if kwargs:
        for button, text in kwargs.items():
            buttons.append(InlineKeyboardButton(text=text, callback_data=button))

    # Распаковка списка с кнопками в билдер методом row c параметром width
    kb_builder.row(*buttons, width=width)

    # Возврат объекта инлайн-клавиатуры
    return kb_builder.as_markup()


def create_inline_kb_test(width: int, *args: str, **kwargs: str) -> InlineKeyboardMarkup:
    # Инициализация билдера
    kb_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
    # Инициализация списка кнопок
    buttons: list[InlineKeyboardButton] = []

    # Заполнение списка кнопками из аргументов args и kwargs
    if args:
        for button in args:
            buttons.append(InlineKeyboardButton(
                text=LEXICON_COMMANDS_RU[button] if button in LEXICON_COMMANDS_RU else button,
                url='https://t.me/V36_bot'))
    if kwargs:
        for button, text in kwargs.items():
            buttons.append(InlineKeyboardButton(text='ПОМОЩЬ', url='https://t.me/V36_bot'))

    # Распаковка списка с кнопками в билдер методом row c параметром width
    kb_builder.row(*buttons, width=width)

    # Возврат объекта инлайн-клавиатуры
    return kb_builder.as_markup()