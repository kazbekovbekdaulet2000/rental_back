import math
from django.db import models
from manage.models.rentinhand_order import RentInHandOrder
from product.models.bag.order import Order
from datetime import datetime, timedelta

def now_minus_30(): return datetime.now() - timedelta(days=28)

class Statistics(models.Model):
    created_at = models.DateTimeField(null=True)
    start_at = models.DateTimeField(null=True)
    end_at = models.DateTimeField(null=True)

# add category filter

    orders = None
    rnh_orders = None

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.rnh_orders = self.init_rnh_orders()
        self.orders = self.init_orders()

    def init_orders(self):
        filter = { }
        if(self.created_at): filter.update({"created_at__gte" : self.created_at})
        if(self.start_at): filter.update({"start_time__gte" : self.start_at})
        else: filter.update({"start_time__gte" : now_minus_30()})
        if(self.end_at): filter.update({"end_time__lte" : self.end_at})

        return Order.objects.filter(**filter)
    
    def init_rnh_orders(self):
        filter = { }
        if(self.start_at): filter.update({"start_time__gte" : self.start_at})
        else: filter.update({"start_time__gte" : now_minus_30()})
        if(self.end_at): filter.update({"end_time__lte" : self.end_at})

        return RentInHandOrder.objects.filter(**filter)

    @property
    def orders_count(self):
        return self.orders.count
    
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
    def rnh_days_count(self):
        days = 0
        for order in self.rnh_orders:
            time = order.end_time - order.start_time
            days += self.total_days(time)
        return days

    @property
    def rnh_orders_count(self):
        return self.rnh_orders.count

    def total_days(self, time):
        days = math.ceil(time.total_seconds() / (24 * 60 * 60))
        if (days == 0): 
            days = 1
        return days

    class Meta:
        managed = False
