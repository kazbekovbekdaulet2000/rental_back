from django.db import models
from common.custom_model import AbstractModel
from manager.constants import ManagerOrderInventoryStatus
from manager.models.inventory.inventory import Inventory
from manager.models.inventory.inventory_tarif import InventoryTarif
from manager.models.order.order import ManagerOrder
from django.utils.translation import gettext_lazy as _


class ManagerOrderInventory(AbstractModel):
    manager_order = models.ForeignKey(
        ManagerOrder,
        on_delete=models.CASCADE, null=False)
    inventory = models.ForeignKey(
        Inventory,
        related_name='order_inventories',
        on_delete=models.DO_NOTHING, null=True
    )
    tarif = models.ForeignKey(
        InventoryTarif,
        related_name='order_inventories',
        on_delete=models.DO_NOTHING, null=True
    )
    status = models.PositiveIntegerField(
        default=ManagerOrderInventoryStatus.RESERVED,
        choices=ManagerOrderInventoryStatus.choices
    )
    price = models.PositiveIntegerField(null=False)

    def save(self, *args, **kwargs):
        self.price = self.tarif.price
        return super().save(*args, **kwargs)

    class Meta:
        ordering = ['-created_at', ]
