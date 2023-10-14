from sqlalchemy import BigInteger, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ..models.base import BaseModel
from ..models.order_goods import OrderGoods


class Goods(BaseModel):
    """
        Модль товаров, которые фигурируют в заказах
    """

    __tablename__ = 'goods'

    id = mapped_column(BigInteger, primary_key=True)
    
    # Название товара
    name: Mapped[str] = mapped_column(Text)
    
    # Ссылка на картинку, может быть NULL
    image: Mapped[str] = mapped_column(
            Text,
            nullable=True,
            )

    # Полезные ссылки на товары для заказов, может быть NULL
    useful_url: Mapped[str] = mapped_column(
            Text,
            nullable=True,
            )

    # Связь с таблицей order_goods
    order_goods: Mapped['OrderGoods'] = relationship(back_populates='goods')

