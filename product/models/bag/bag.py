from django.db import models
from common.custom_model import AbstractModel
from product.models.service import Service
import uuid


class UserBag(AbstractModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    previous_order = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.id} ({', '.join(list(self.products.all().values_list('product__name_ru', flat=True)))})"

    @property 
    def services(self):
        return Service.objects.filter(id__in=self.products.values_list('product__services__service', flat=True))
    
    @property 
    def services__str(self):
        return ", ".join(self.services.values_list('name_ru', flat=True))
    
    @property
    def services_price(self):
        return sum(self.services.values_list('daily_price', flat=True))

    @property
    def products_price(self):
        return sum(map(lambda res: (res[0] * res[1]), self.products.values_list('product__daily_price', 'count')))

    @property
    def total_price(self):
        return self.services_price + self.products_price

    class Meta:
        verbose_name = 'Корзина пользователя'
        verbose_name_plural = 'Корзина пользователей'
        ordering = ['-created_at']

