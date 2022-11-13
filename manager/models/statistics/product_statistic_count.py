from django.db import models
from product.models.product import Product

    
class ManagerProductCountStat(models.Model):
    product = models.ForeignKey(Product, models=models.CASCADE)
    rent_count = models.PositiveIntegerField()
    order_count = models.PositiveIntegerField()

    class Meta: 
        managed = False