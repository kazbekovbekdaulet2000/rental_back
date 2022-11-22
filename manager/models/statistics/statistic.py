from django.db import models
from common.default_time import now_minus_28
from manager.models.rentinhand_order import ManagerRentInHandOrder
from product.models.bag.order import Order


class ManagerStat(models.Model):
    start_at = models.DateTimeField(null=True)
    end_at = models.DateTimeField(null=True)

    orders = None
    rnh_orders = None

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        filter, rnh_filter = {}, {}

        if (self.start_at):
            filter.update({"created_at__gte": self.start_at})
            rnh_filter.update({"end_time__gte": self.start_at})
        else:
            filter.update({"created_at__gte": now_minus_28()})
            rnh_filter.update({"end_time__gte": now_minus_28()})

        if (self.end_at):
            filter.update({"created_at__lte": self.end_at})
            rnh_filter.update({"end_time__lte": self.end_at})

        self.orders = Order.objects.filter(**filter)
        self.rnh_orders = ManagerRentInHandOrder.objects.filter(**rnh_filter)

    @property
    def orders_count(self):
        return self.orders.count

    @property
    def rnh_orders_count(self):
        return self.rnh_orders.count

    @property
    def orders_price(self):
        sum = 0
        for order in self.orders:
            sum += order.products_price
        return sum

    @property
    def rnh_orders_price(self):
        return sum(self.rnh_orders.values_list('sum_rental', flat=True))

    class Meta:
        managed = False
