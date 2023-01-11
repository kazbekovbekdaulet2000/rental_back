from django.db import models
from common.custom_model import AbstractModel
from manager.models.interchangeable.interchangeable import Interchangeable
from django.utils.translation import gettext_lazy as _
from product.models.product import Product


class ProductPart(AbstractModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="parts")
    part = models.ForeignKey(Interchangeable, on_delete=models.CASCADE, related_name='products')
    count = models.PositiveSmallIntegerField(default=1)