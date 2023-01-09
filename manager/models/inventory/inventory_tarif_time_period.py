from django.db import models
from common.custom_model import AbstractModel
from django.utils.translation import gettext_lazy as _


# TODO
class InventoryTarifTimePeriod(AbstractModel):
    time = models.DurationField(null=False)
    
    class Meta:
        ordering = ('-created_at', )
