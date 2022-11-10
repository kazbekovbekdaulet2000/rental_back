from django.db import models
from django.contrib.postgres.fields import ArrayField


class RentInHandOrder(models.Model):
    order_id = models.BigIntegerField(null=True)
    sum_rental = models.BigIntegerField(null=False)
    start_time = models.DateTimeField(null=False)
    end_time = models.DateTimeField(null=False)
    file_data = models.JSONField(null=False)
    file = models.FileField(null=True)
    inventories = ArrayField(base_field=models.PositiveIntegerField(), null=True, blank=True)