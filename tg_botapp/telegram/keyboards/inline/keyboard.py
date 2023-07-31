from aiogram import Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message, KeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder

from tg_botapp.telegram.lexicon.lexicon import LEXICON_COMMANDS_RU, LEXICON_ADMIN

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


# Функция генерит еще одну клавиатуру - вложенную
def create_inline_kb_inside(width: int, *args: str, **kwargs: str) -> InlineKeyboardMarkup:
    # Инициализация билдера
    kb_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
    # Инициализация списка кнопок
    buttons: list[InlineKeyboardButton] = []

    # Заполнение списка кнопками из аргументов args и kwargs
    if args:
        for button in args:
            buttons.append(InlineKeyboardButton(
                text=LEXICON_COMMANDS_RU[button] if button in LEXICON_COMMANDS_RU else button,
                url='https://t.me/zov_it_mvbot'))
    if kwargs:
        for button, text in kwargs.items():
            buttons.append(InlineKeyboardButton(text='ПОМОЩЬ', url='https://t.me/zov_it_mvbot'))

    # Распаковка списка с кнопками в билдер методом row c параметром width
    kb_builder.row(*buttons, width=width)

    # Возврат объекта инлайн-клавиатуры
    return kb_builder.as_markup()


# Создаем кнопки для Админа
button_sos: KeyboardButton = KeyboardButton(text=LEXICON_ADMIN['DELETE_MESSAGE'])

# Инициализируем билдер для клавиатуры ADMIN"
admin_menu_b: ReplyKeyboardBuilder = ReplyKeyboardBuilder()

# Добавляем кнопки в билдер с параметром width=2 для Админа
admin_menu_b.row(button_sos, width=2)

# Создаем клавиатуру ADMIN
admin_menu = admin_menu_b.as_markup(one_time_keyboard=True, resize_keyboard=True)