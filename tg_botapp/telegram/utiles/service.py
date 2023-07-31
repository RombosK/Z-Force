from aiogram.types import Message
from asyncio import sleep
from ..config_data.config import Config, load_config

# Загружаем конфиг в переменную config
config: Config = load_config()
sleep_time: int = config.tg_bot.sleep_time


# Функция удаления сообщения через заданное в .env время
async def msg_to_delete(message: Message) -> None:
    await sleep(sleep_time)
    await message.delete()
