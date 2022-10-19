from django.db import models
from common.custom_model import AbstractModel
from django.utils.translation import gettext_lazy as _
from product.models.product import Product
from product.models.service import Service


class ProductService(AbstractModel):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name="services", on_delete=models.CASCADE)  
    required = models.BooleanField(default=False)

    def __str__(self):
        return self.service.name_ru

    class Meta:
        ordering = ('created_at',)
        verbose_name = 'Товар (Сервис)'
        verbose_name_plural = 'Товары (Сервис)'
