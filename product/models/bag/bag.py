from django.db import models
from common.custom_model import AbstractModel
from product.models.service import Service
import uuid
from django.utils import timezone

class UserBag(AbstractModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    previous_order = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    delivery = models.BooleanField(default=False, null=False)
     
    services = None
    services_price = None
    services__str = None
    products_price = None
    total_price = None
    discount = None
    delivery_price = 0
    timezone = None

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.services = Service.objects.filter(id__in=self.products.values_list('product__services__service', flat=True))
        self.services_price = sum(self.services.values_list('daily_price', flat=True))
        self.services__str = ", ".join(self.services.values_list('name_ru', flat=True))
        self.products_price = self.init_products_price()

        if(self.delivery and self.products.count() > 0):
            self.delivery_price = 2500 
        else:
            self.delivery_price = 0 
            
        self.total_price = self.services_price + self.products_price + self.delivery_price
    
    def init_products_price(self):
        list = []

        for item in self.products.all():
            product = item.product
            count = item.count
            _discount = product.discounts.filter(discount__start_date__lte=timezone.now(), discount__end_date__gte=timezone.now()).last()
            if(_discount and _discount.discount.start_date <= self.updated_at and _discount.discount.end_date >= self.updated_at):
                list.append([product.daily_price * _discount.discount_multiplier, count])
            else:
                list.append([product.daily_price, count])

        return sum(map(lambda res: (res[0] * res[1]), list))

    def __str__(self):
        return f"{self.id} ({', '.join(list(self.products.all().values_list('product__name_ru', flat=True)))})"

    class Meta:
        verbose_name = 'Корзина пользователя'
        verbose_name_plural = 'Корзина пользователей'
        ordering = ['-created_at']

