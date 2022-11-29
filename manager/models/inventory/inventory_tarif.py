from django.db import models
from common.custom_model import AbstractModel
from django.core.validators import MaxValueValidator
from auditlog.registry import auditlog
from auditlog.models import AuditlogHistoryField


TARIF_TYPES = (
    (0, 'В Процентах'),
    (1, 'В Цене')
)


class InventoryTarif(AbstractModel):
    type = models.PositiveIntegerField(choices=TARIF_TYPES)
    increase_price = models.PositiveIntegerField(null=True)
    decrease_price = models.PositiveIntegerField(null=True)
    increase_price_percentage = models.PositiveIntegerField(
        null=True,
        validators=(MaxValueValidator(99), )
    )
    decrease_price_percentage = models.PositiveIntegerField(
        null=True,
        validators=(MaxValueValidator(99), )
    )
    history = AuditlogHistoryField()


auditlog.register(InventoryTarif)