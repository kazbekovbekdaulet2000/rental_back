from django.db import models
from common.custom_model import AbstractModel
from manager.models.inventory.inventory_tarif import InventoryTarif
from django.utils.translation import gettext_lazy as _


# TODO
class InventoryTarifPeriod(AbstractModel):
    tarif = models.ForeignKey(InventoryTarif, on_delete=models.CASCADE)
    time = models.DurationField(null=False)
    price = models.PositiveIntegerField(null=False)

    class Meta:
        ordering = ('-created_at', )
