from django.db import models
from django.contrib.postgres.fields import ArrayField


class ManagerRentInHandOrder(models.Model):
    order_id = models.BigIntegerField(null=False)
    sum_rental = models.BigIntegerField(null=False)
    # times
    start_time = models.DateTimeField(null=False)
    end_time = models.DateTimeField(null=False)
    created_at = models.DateTimeField(null=False)
    
    file_data = models.JSONField(null=False)
    file = models.FileField(null=True, default=None)
    inventories = ArrayField(base_field=models.PositiveIntegerField(), null=True, blank=True)

    class Meta: 
        db_table = 'rent_in_hand_orders'