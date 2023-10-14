from datetime import datetime
from typing import Optional, List

from sqlalchemy import BigInteger, Boolean, DateTime, String, Text
from sqlalchemy import func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ..models.base import BaseModel, UserStatus
from ..models.black_list import BlackList

class User(BaseModel):
    """
        Модель пользоателя
    """
    
    __tablename__ = 'user'

    id = mapped_column(BigInteger, primary_key=True)

    # Имя
    first_name: Mapped[str] = mapped_column(
            String(30),
            )
    
    # Фамилия, может быть NULL
    last_name: Mapped[Optional[str]] = mapped_column(
            String(50),
            nullable=True,
            )
    
    # Статус выбирается из возможных вариантов модели UserStatus
    status: Mapped[UserStatus] = mapped_column()

    # Статус активности клиента, может быть NULL
    is_active: Mapped[bool] = mapped_column(
            Boolean,
            default=True,
            )

    # Поле для дополнительной информации
    info: Mapped[Optional[str]] = mapped_column(
            Text,
            nullable=True,
            )
    
    # Дата создания, не может быть пустой, по умолчанию текущее время создания
    created_at: Mapped[datetime] = mapped_column(
            DateTime,
            nullable=False,
            default=func.now(),
            )

    # Дата изменения, может быть пустой
    edited_at: Mapped[Optional[datetime]] = mapped_column(
            DateTime,
            nullable=True,
            server_default=func.current_timestamp(),
            )

    # Признак, что запись удалена из системы, по умолчанию False 
    is_deleted: Mapped[bool] = mapped_column(
            Boolean,
            default=False,
            )
    
    # Связь с таблицей black_list
    black_list: Mapped[List['BlackList']] = relationship(
            back_populates='user'
            )

