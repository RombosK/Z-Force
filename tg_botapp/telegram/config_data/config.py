from __future__ import annotations

from dataclasses import dataclass
from environs import Env


@dataclass
class DatabaseConfig:
    database: str         # Название базы данных
    db_host: str          # URL-адрес базы данных
    db_user: str          # Username пользователя базы данных
    db_password: str      # Пароль к базе данных


@dataclass
class TgBot:
    token: str # Токен для доступа к телеграм-боту
    admin_ids: list[int]  # Список id администраторов бота
    sleep_time: int # Время задержки перед удалением


@dataclass
class Config:
    tg_bot: TgBot
    db: DatabaseConfig


def load_config(path: str | None = None) -> Config:

    env: Env = Env()
    env.read_env(path)

    return Config(tg_bot=TgBot(token=env('BOTV_TOKEN'),
                               admin_ids=list(map(int, env.list('ADMIN_IDS'))),
                               sleep_time=list(map(int, env.list('DELETE_MSG_DELAY')))[0]),
                  db=DatabaseConfig(database=env('DATABASE'),
                                    db_host=env('DB_HOST'),
                                    db_user=env('DB_USER'),
                                    db_password=env('DB_PASSWORD')),
                  )
