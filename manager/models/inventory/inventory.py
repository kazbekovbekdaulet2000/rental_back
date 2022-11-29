from django.db import models
from common.custom_model import AbstractModel
from manager.models.inventory.inventory_status import InventoryStatus
from manager.models.inventory.inventory_tarif import InventoryTarif
from product.models.product import Product
from auditlog.registry import auditlog
from auditlog.models import AuditlogHistoryField


class Inventory(AbstractModel):
    unique_id = models.CharField(max_length=32)
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING, related_name='inventories')
    status = models.ForeignKey(InventoryStatus, on_delete=models.DO_NOTHING)
    buy_price = models.PositiveIntegerField(null=True)
    buy_date = models.DateField(null=True)
    tarif = models.ForeignKey(InventoryTarif, on_delete=models.SET_NULL, null=True)
    history = AuditlogHistoryField()

    class Meta:
        unique_together = ('unique_id', 'product')


auditlog.register(Inventory)