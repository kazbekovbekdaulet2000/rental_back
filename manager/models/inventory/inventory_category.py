from django.db import models
from common.custom_model import AbstractModel


class InventoryCategory(AbstractModel):
    name = models.CharField(max_length=255)
    comment = models.TextField(max_length=512, null=True)
    prefix = models.CharField(max_length=16, null=False)
    