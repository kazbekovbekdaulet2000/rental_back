# from django.db import models
# from common.custom_model import AbstractModel
# from django.utils.translation import gettext_lazy as _
# from django.core.validators import MaxValueValidator


# class ProductDiscount(AbstractModel):
#     start_date = models.DateTimeField(verbose_name=_('Начало Акции'), null=False)
#     end_date = models.DateTimeField(verbose_name=_('Конец Акции'), null=False)
#     discount_percent = models.PositiveIntegerField(validators=(MaxValueValidator(99),))

#     class Meta:
#         verbose_name = 'Скидка'
#         verbose_name_plural = 'Скидки'
