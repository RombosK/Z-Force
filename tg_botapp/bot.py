import asyncio
import logging
from aiogram import Bot, Dispatcher

from telegram.config_data.config import Config, load_config
from telegram.handlers import other_handlers, user_handlers, admin_handlers

# Инициализируем логгер
from telegram.keyboards.set_menu import set_main_menu

logger = logging.getLogger(__name__)


# Функция конфигурирования и запуска бота
async def main() -> None:

    # Кофигурируем логирование
    logging.basicConfig(
        level=logging.INFO,
        format='%(filename)s:%(lineno)d #%(levelname)-8s '
        '[%(asctime)s] - %(name)s - %(message)s'
    )
    # Выводим в консоль информацию о начале запуска
    logger.info('Starting BOTV')

    # Загружаем конфиг в переменную config
    config: Config = load_config()

    # Инициализируем бот и диспетчер
    bot: Bot = Bot(token=config.tg_bot.token, parse_mode='HTML')
    dp: Dispatcher = Dispatcher()

    # Настраиваем кнопку Menu
    await set_main_menu(bot)

    # Регистриуем роутеры в диспетчере
    # dp.include_router(admin_handlers.router)
    # dp.include_router(user_handlers.router)
    dp.include_router(other_handlers.router)

    # Пропускаем накопившиеся апдейты и запускаем polling
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())




