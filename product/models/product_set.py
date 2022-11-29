from django.db import models
from common.custom_model import AbstractModel
from django.utils.translation import gettext_lazy as _
from product.models.product import Product


class ProductSet(AbstractModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="set")
    set_product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="set_objects")
    count = models.PositiveIntegerField(default=1)

    class Meta:
        ordering = ('created_at',)
        verbose_name = 'Сет продукт'
        verbose_name_plural = 'Сет продукт'
