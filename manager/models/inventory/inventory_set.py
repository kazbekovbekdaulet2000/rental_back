from django.db import models
from common.custom_model import AbstractModel
from manager.models.interchangeable.interchangeable import Interchangeable
from manager.models.inventory.inventory_category import InventoryCategory


class InventorySet(AbstractModel):
    name = models.CharField(max_length=255)
    unique_id = models.CharField(max_length=32, unique=True, null=True)
    category = models.ForeignKey(InventoryCategory, on_delete=models.CASCADE, null=True)

    class Meta:  
        ordering = ('-created_at', )


class InventorySetItem(AbstractModel):
    set = models.ForeignKey(InventorySet, on_delete=models.CASCADE, related_name="items")
    interchangeable = models.ForeignKey(Interchangeable, on_delete=models.CASCADE)
    tarif_price = models.IntegerField(null=False)
    count = models.PositiveSmallIntegerField()

    class Meta:  
        ordering = ('-created_at', )