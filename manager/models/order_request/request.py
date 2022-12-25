from django.db import models
from common.custom_model import AbstractModel
from manager.constants import OrderRequestStatus
from manager.models.clients.client import Client


class OrderRequest(AbstractModel):
    client = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True)
    status = models.PositiveSmallIntegerField(choices=OrderRequestStatus.choices, default=OrderRequestStatus.REQUEST)
    rent_start = models.DateTimeField(null=False)
    rent_end = models.DateTimeField(null=False)
    rent_fact_start = models.DateTimeField(null=True)
    rent_fact_end = models.DateTimeField(null=True)

    # price
    price = models.PositiveIntegerField(null=True)
    price_discount = models.PositiveIntegerField(null=True)

    class Meta:
        ordering = ('-created_at', )
