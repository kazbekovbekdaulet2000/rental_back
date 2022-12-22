from django.db import models
from common.custom_model import AbstractModel
from manager.models.interchangeable.interchangeable import Interchangeable


class InventorySet(AbstractModel):
    name = models.CharField(max_length=255)


class InventorySetItem(AbstractModel):
    set = models.ForeignKey(InventorySet, on_delete=models.CASCADE, related_name="items")
    interchangeable = models.ForeignKey(Interchangeable, on_delete=models.CASCADE)
    count = models.PositiveSmallIntegerField()
