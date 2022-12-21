from django.db import models
from common.custom_model import AbstractModel
from manager.constants import InventoryStatusType


class InventoryStatus(AbstractModel):
    name = models.CharField(max_length=255)
    comment = models.TextField(max_length=512, null=True)
    status = models.PositiveSmallIntegerField(default=InventoryStatusType.FREE, choices=InventoryStatusType.choices)
    disable = models.BooleanField(default=False)