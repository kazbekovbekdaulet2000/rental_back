from typing import List
from django.db import models
from common.custom_model import AbstractModel
from manager.models.inventory.inventory import Inventory
import random

class Interchangeable(AbstractModel):
    name = models.CharField(max_length=255)
    inventories = models.ManyToManyField(Inventory, related_name="product_parts")

    # non db fields
    options = []

    def have_free_inventories(self, start_at, end_at, count) -> bool:
        self.options = []
        for inventory in self.inventories.all():
            if inventory.is_free(start_at, end_at):
                self.options.append(inventory)
        if(len(self.options) < count):
            return False
        return True

    def get_free_inventories(self, count) -> List[Inventory]:
        return random.choices(self.options, k=count)

    def __str__(self):
        return self.name

    class Meta:  
        ordering = ('-created_at', )