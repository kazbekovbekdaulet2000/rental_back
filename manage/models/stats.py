from django.db import models
from product.models.bag.order import Order
from datetime import datetime, timedelta

def now_minus_30(): return datetime.now() - timedelta(days=28)

class Statistics(models.Model):
    created_at = models.DateTimeField(null=True)
    start_at = models.DateTimeField(null=True)
    end_at = models.DateTimeField(null=True)

# add category filter

    orders = None
    approved_orders = None

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.orders = self.init_orders()
        self.approved_orders = self.orders.filter(approved=True)

    def init_orders(self):
        filter = { }
        if(self.created_at): filter.update({"created_at__gte" : self.created_at})
        if(self.start_at): filter.update({"start_time__gte" : self.start_at})
        else: filter.update({"start_time__gte" : now_minus_30()})
        if(self.end_at): filter.update({"end_time__lte" : self.end_at})

        return Order.objects.filter(**filter)
    
    @property
    def orders_count(self):
        return self.orders.count
    
    @property
    def approved_orders_count(self):
        return self.approved_orders.count
    
    @property
    def products_value(self):
        products_sum = 0
        for order in self.approved_orders:
            products_sum += order.products_price
        return products_sum

    @property
    def services_value(self):
        services_sum = 0
        for order in self.approved_orders: services_sum += order.services_price
        return services_sum

    @property
    def total_days_count(self):
        days = 0
        for order in self.orders: days += order.total_days
        return days
        
    @property
    def approved_days_count(self):
        days = 0
        for order in self.approved_orders:
            days += order.total_days
        return days

    class Meta:
        managed = False
