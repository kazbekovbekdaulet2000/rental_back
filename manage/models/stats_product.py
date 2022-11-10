import math
from django.db import models
from manage.models.stats_product_count import ProductCountStatistics
from product.models.bag.order import Order
from product.models.product import Product
from datetime import datetime, timedelta


def now_minus_30(): return datetime.now() - timedelta(days=28)


class ProductStatistics(models.Model):
    start_at = models.DateTimeField(null=True)
    end_at = models.DateTimeField(null=True)

    products = None
    products_days_count_dict = {}
    products_order_count_dict = {}
    product_count = list()

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        objs = {}
        days_dict = {}
        filter = {"approved": True}
        if (self.start_at):
            filter.update({"start_time__gte": self.start_at})
        else:
            filter.update({"start_time__gte": now_minus_30()})
        if (self.end_at):
            filter.update({"end_time__lte": self.end_at})

        for productId, days, start_time, end_time in (Order.objects.filter(**filter).values_list('bag__products__product', 'bag__products__count', 'start_time', 'end_time')):
            if (str(productId) in objs.keys()):
                objs.update({str(productId): str((int(days) * self.get_days(start_time, end_time))  + int(objs[str(productId)]))})
                days_dict.update({str(productId): str(int(self.get_days(start_time, end_time)) + int(days_dict[str(productId)]))})
            else:
                objs.update({str(productId): str(days * self.get_days(start_time, end_time))})
                days_dict.update({str(productId): str(self.get_days(start_time, end_time))})

        self.products_days_count_dict = objs
        self.products_order_count_dict = days_dict
        self.products = Product.objects.filter(id__in=list(objs.keys()))
        self.product_count = list()
        for product in self.products:
            self.product_count.append(ProductCountStatistics(
                id=None,
                product=product,
                total_days_count=int(self.products_days_count_dict.get(str(product.id))),
                total_orders_count=int(self.products_order_count_dict.get(str(product.id)))
            ))

    def get_days(self, start_time, end_time):
        days = math.ceil((end_time - start_time).total_seconds() / (24 * 60 * 60))
        if (days == 0): 
            days = 1
        return days

    class Meta:
        managed = False
