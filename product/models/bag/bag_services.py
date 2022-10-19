from django.db import models
from common.custom_model import AbstractModel
from product.models.bag.bag import UserBag
from product.models.product import Product


class UserBagServices(AbstractModel):
    order = models.ForeignKey(UserBag, related_name='services', on_delete=models.CASCADE)
    count = models.PositiveIntegerField(default=1)
    service = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.order.id}: {self.product.__str__()}"

    def telegram_detail(self, order, days):
        return f"""<b>{order}. {self.product.name_ru}</b> (артикул: {self.product.articule}) \nКол-во: <b>{self.count}</b>\nСтоимость: {self.product.daily_price} KZT x {self.count} шт x {days} суток = <b>{self.product.daily_price * self.count * days} KZT</b>\n\n"""

    class Meta:
        ordering=['-created_at']
