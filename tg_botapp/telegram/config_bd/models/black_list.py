from datetime import datetime

from sqlalchemy import BigInteger, DateTime, ForeignKey, Text, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ..models.base import BaseModel
#from ..models.user import User


class BlackList(BaseModel):
    """
        Модель ченрый список, для сбора данных о нежелательных пользователях
    """

    __tablename__ = 'black_list'

    id = mapped_column(BigInteger, primary_key=True)

    # Пользователь которого забанили
    user_id: Mapped[int] = mapped_column(BigInteger, ForeignKey('user.id'))
    
    # Дата создания записи, по умолчанию текущее время
    created_at: Mapped[datetime] = mapped_column(
            DateTime,
            nullable=False,
            default=func.now(),
            )    

    # Описание
    description: Mapped[str] = mapped_column(Text)

    # Подстверждение, ссылка на скриншот с обоснованием
    substantiation: Mapped[str] = mapped_column(Text)

    # Связь с таблицей user
    user: Mapped['User'] = relationship(back_populates='black_list')

