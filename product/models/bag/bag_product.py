from django.db import models
from common.custom_model import AbstractModel
from product.models.bag.bag import UserBag
from product.models.product import Product


class UserBagItem(AbstractModel):
    order = models.ForeignKey(UserBag, related_name='products', on_delete=models.CASCADE)
    count = models.PositiveIntegerField(default=1)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.order.id}: {self.product.__str__()}"

    def telegram_detail(self, order, days):
        if(self.product.discount):
            return f"""<b>{order}. {self.product.name_ru}</b> (артикул: {self.product.articule}) \n<b>Скидка: {self.product.discount}%</b>\nКол-во: <b>{self.count}</b>\nСтоимость: {self.product.price}KZT ({self.product.daily_price}KZT) x {self.count} шт x {days} суток = <b>{self.product.price * self.count * days} KZT</b>\n\n"""
        return f"""<b>{order}. {self.product.name_ru}</b> (артикул: {self.product.articule}) \nКол-во: <b>{self.count}</b>\nСтоимость: {self.product.price} KZT x {self.count} шт x {days} суток = <b>{self.product.price * self.count * days} KZT</b>\n\n"""

    class Meta:
        ordering=['created_at']
