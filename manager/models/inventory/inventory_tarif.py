from django.db import models
from common.custom_model import AbstractModel
from auditlog.registry import auditlog
from auditlog.models import AuditlogHistoryField
from manager.models.inventory.inventory import Inventory
from manager.models.inventory.inventory_set import InventorySetItem
from manager.models.inventory.inventory_tarif_time_period import InventoryTarifTimePeriod
from product.models.product import Product
from django.utils.translation import gettext_lazy as _


class InventoryTarif(AbstractModel):
    default = models.BooleanField(default=False)
    name = models.CharField(max_length=255, default="name")
    inventory = models.ForeignKey(Inventory, on_delete=models.CASCADE, related_name="tarifs", default=None, null=True)
    inventory_set = models.ForeignKey(InventorySetItem, on_delete=models.CASCADE, related_name="tarifs", default=None, null=True)
    price = models.PositiveIntegerField(null=False, default=0)
    product_set = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    time_period = models.ForeignKey(InventoryTarifTimePeriod, on_delete=models.CASCADE, null=True)
    
    history = AuditlogHistoryField()

    def __str__(self):
        return f"{self.name} ({self.price})"

    class Meta: 
        ordering = ('-created_at', )        
        unique_together = ('default', 'inventory', 'price')


auditlog.register(InventoryTarif)
