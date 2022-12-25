from django.db import models
from common.custom_model import AbstractModel
from manager.models.order_request.request import OrderRequest
from product.models.product_discount import ProductDiscount
from product.models.service import Service


class OrderRequestService(AbstractModel):
    request = models.ForeignKey(OrderRequest, on_delete=models.SET_NULL, null=True)

    # inventory - discount - tarif
    service = models.ForeignKey(Service, on_delete=models.SET_NULL, null=True)
    discount = models.ForeignKey(ProductDiscount, on_delete=models.SET_NULL, null=True)
    
    # price
    price = models.PositiveIntegerField(null=True)
    price_discount = models.FloatField(null=True)
    
    def save(self, *args, **kwargs) -> None:
        # update of price
        return super().save(*args, **kwargs)

    class Meta:
        ordering = ('-created_at', )