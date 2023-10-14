from enum import Enum as en

from sqlalchemy import BigInteger, ForeignKey, Integer, Enum, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ..models.base import BaseModel
#from ..models.order import Order
#from ..models.goods import Goods


class OrderGoodsStatus(en):
    
    UNPROCESSED = 0 # Необработанный товар
    IN_PROGRES = 1  # Товар в проработке
    COMPLITE = 2    # Товар выполнен
    CANCELED = 3    # Товар отменен 


class OrderGoods(BaseModel):
    """
        Модель товары заказов
    """

    __tablename__ = 'order_goods'

    id = mapped_column(BigInteger, primary_key=True)
    
    # Статус обработки товара в заказе
    status: Mapped[OrderGoodsStatus] = mapped_column()

    # Требуемое количество товара
    quantity: Mapped[int] = mapped_column(Integer)

    # Единицы измерения количества
    unit: Mapped[str] = mapped_column(String(4))

    # Идентификатор заказа
    order_id: Mapped[int] = mapped_column(BigInteger, ForeignKey('order.id'))

    # Идентификатор товара
    goods_id: Mapped[int] = mapped_column(BigInteger, ForeignKey('goods.id'))

    # Связь с таблицей order
    order: Mapped['Order'] = relationship(back_populates='oreder_goods')

    # Связь с таблицей goods
    goods: Mapped['Goods'] = relationship(back_populates='order_goods')

