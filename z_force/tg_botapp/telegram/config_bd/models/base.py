from enum import Enum

from sqlalchemy.orm import DeclarativeBase


class UserStatus(Enum):
    """
        Класс-перечисление статусов пользователя
    """

    ADMIN = "admin"
    ANONIM = "anonim"
    REGISTRED = "registred"
    MODERATOR = "moderator"


class BaseModel(DeclarativeBase):
    """
        Базовый класс для моделей. Здесь, в случае необходимости,
        можно будет определять общие для всех моделей атрибуты и 
        правила.
    """
    pass  


