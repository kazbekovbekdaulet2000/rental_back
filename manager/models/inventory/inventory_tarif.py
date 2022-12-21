from django.db import models
from common.custom_model import AbstractModel
from auditlog.registry import auditlog
from auditlog.models import AuditlogHistoryField
from manager.models.inventory.inventory import Inventory
from product.models.product import Product


class InventoryTarif(AbstractModel):
    default = models.BooleanField(default=False)
    name = models.CharField(max_length=255, default="name")
    inventory = models.ForeignKey(Inventory, on_delete=models.CASCADE, related_name="tarifs", default=None, null=True)
    price = models.PositiveIntegerField(null=False, default=0)
    product_set = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)

    history = AuditlogHistoryField()

    def __str__(self):
        return f"{self.inventory.__str__()} - {self.name} ({self.price})"

    class Meta:
        unique_together = ('default', 'inventory', 'price')


auditlog.register(InventoryTarif)
