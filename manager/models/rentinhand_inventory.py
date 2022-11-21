from django.db import models


class ManagerRentInHandInventory(models.Model):
    rnh_id = models.CharField(max_length=255, null=True, blank=True)
    title = models.CharField(max_length=5192, null=False)
    amount_rent_sum = models.BigIntegerField(null=True)
    price = models.CharField(max_length=5192, null=False)
    
    class Meta: 
        db_table = 'rent_in_hand_inventories'