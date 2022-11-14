from django.db import models
from django.utils.translation import gettext_lazy as _
from product.models.product import Product
from common.custom_model import AbstractModel


class ProductAnnouncement(AbstractModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.PositiveIntegerField(null=False)
    
    def __str__(self):
        return f"{self.product.__str__()} - {self.order}"

    class Meta:
        ordering = ('order',)
        verbose_name = 'Новый продукт'
        verbose_name_plural = 'Новые продукты'
