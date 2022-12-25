from django.db import models
from common.custom_model import AbstractModel
from manager.models.inventory.inventory import Inventory
from manager.models.inventory.inventory_tarif import InventoryTarif
from manager.models.order_request.request import OrderRequest
from product.models.product_discount import ProductDiscount


class OrderRequestInventory(AbstractModel):
    request = models.ForeignKey(OrderRequest, on_delete=models.SET_NULL, null=True)

    # inventory - discount - tarif
    inventory = models.ForeignKey(Inventory, on_delete=models.SET_NULL, null=True)
    discount = models.ForeignKey(ProductDiscount, on_delete=models.SET_NULL, null=True)
    tarif = models.ForeignKey(InventoryTarif, on_delete=models.SET_NULL, null=True)
    
    # price
    price = models.PositiveIntegerField(null=True)
    price_discount = models.FloatField(null=True)
    
    def save(self, *args, **kwargs) -> None:
        # update of price
        return super().save(*args, **kwargs)

    class Meta:
        ordering = ('-created_at', )

# post save to update whole request to update overall price