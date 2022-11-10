from django.db import models
from product.models.product import Product


class ProductCountStatistics(models.Model):
    product = models.ForeignKey(Product, null=False, on_delete=models.DO_NOTHING)
    total_days_count = models.PositiveIntegerField()        
    total_orders_count = models.PositiveIntegerField()        

    @property
    def money_amount(self):
        return self.total_days_count * self.product.daily_price
    
    class Meta:
        managed = False
