from django.db import models
from common.custom_model import AbstractModel
from django.utils.translation import gettext_lazy as _


class ProductDiscount(AbstractModel):
    name = models.CharField(max_length=255)
    start_date = models.DateTimeField(verbose_name=_('Начало Акции'), null=False)
    end_date = models.DateTimeField(verbose_name=_('Конец Акции'), null=False)

    class Meta:
        db_table = 'product_discount'
        verbose_name = 'Скидка'
        verbose_name_plural = 'Скидки'
