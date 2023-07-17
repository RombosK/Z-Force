from datetime import datetime

from sqlalchemy import BigInteger, DateTime, Integer
from sqlalchemy.orm import Mapped, mapped_column

from ..models.base import BaseModel


class BotMessage(BaseModel):
    """
        Модель сообщений бота
    """

    __tablename__ = 'bot_messages'
    
    # Идентификатор сообщения бота
    botmessage_id: Mapped[int] = mapped_column(BigInteger, primary_key=True)

    # Идентификатор чата куда бот отправил сообщение
    chat_id: Mapped[int] = mapped_column(Integer)

    # Время отправки сообщения ботом
    time: Mapped[datetime] = mapped_column(DateTime)

