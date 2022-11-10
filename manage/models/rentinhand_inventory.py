from django.db import models


class RentInHandInventory(models.Model):
    title = models.CharField(max_length=5192, null=False)
    amount_rent_sum = models.BigIntegerField(null=True)
    price = models.CharField(max_length=5192, null=False)
