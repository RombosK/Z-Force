from datetime import datetime
from enum import Enum as en

from sqlalchemy import BigInteger, DateTime, Enum, ForeignKey, Text
from sqlalchemy import func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ..models.base import BaseModel
from ..models.user import User
from ..models.order_goods import OrderGoods


class OrderStatus(en):
    """
        Класс-перечисление статуса заказа
    """
    UNPROCESSED = 0 # Необработанный заказ
    REGISTRED = 1   # Заказа зарегистрирован
    IN_PROGRES = 2  # Заказ в проработке
    COMPLITE = 3    # Заказ выполнен
    CANCELED = 4    # Заказ отменен


class Order(BaseModel):
    """
        Модель заказов
    """

    __tablename__ = 'order'

    id = mapped_column(BigInteger, primary_key=True)
    
    # Описание заказа, дополнительная информация
    description: Mapped[str] = mapped_column(
            Text,
            nullable=False,
            )
    
    # Дата создания заказа
    created_at: Mapped[datetime] = mapped_column(
            DateTime,
            nullable=False,
            default=func.now(),
            )
    
    # Стату заказа
    status: Mapped[OrderStatus] = mapped_column()
    
    # Заказчик заказа
    customer_id: Mapped[int] = mapped_column(
            BigInteger, 
            ForeignKey('user.id')
            )

    # Ответственный исполнитель
    implementer_id: Mapped[int] = mapped_column(
            BigInteger,
            ForeignKey('user.id')
            )

    # Связь с таблицей user
    customer: Mapped['User'] = relationship(
            'User',
            foreign_keys=[customer_id]
            )
    implementer: Mapped['User'] = relationship(
            'User',
            foreign_keys=[implementer_id]
            )

    # Связь с таблицей order_goods
    order_goods: Mapped['OrderGoods'] = relationship(back_populates='order')

