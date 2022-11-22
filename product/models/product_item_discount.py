from django.db import models
from common.custom_model import AbstractModel
from django.utils.translation import gettext_lazy as _
from django.core.validators import MaxValueValidator
from product.models.product import Product
from product.models.product_discount import ProductDiscount


class ProductItemDiscount(AbstractModel):
    discount = models.ForeignKey(ProductDiscount, related_name="discount_items", on_delete=models.CASCADE)
    discount_percent = models.PositiveIntegerField(validators=(MaxValueValidator(99),))
    products = models.ManyToManyField(Product, related_name="discounts")

    @property
    def discount_multiplier(self):
        return (100 - self.discount_percent) / 100

    class Meta:
        db_table = 'product_discount_item'
        verbose_name = 'Скидка'
        verbose_name_plural = 'Скидки'
