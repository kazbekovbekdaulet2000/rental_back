from django.db import models
from common.custom_model import AbstractModel
from manager.models.inventory.inventory import Inventory

class InventorySchedule(AbstractModel):
    inventory = models.ForeignKey(Inventory, on_delete=models.CASCADE, related_name="schedule", null=False)
    start_at = models.DateTimeField(null=False)
    end_at = models.DateTimeField(null=False)
    completed = models.BooleanField(default=False)
    
    def __str__(self) -> str:
        return f"({self.start_at} - {self.end_at})"

    class Meta:  
        ordering = ('-created_at', )