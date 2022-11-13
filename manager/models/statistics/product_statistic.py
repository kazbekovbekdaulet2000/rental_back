import math
from django.db import models
from common.default_time import now_minus_28
from manager.models.rentinhand_inventory import ManagerRentInHandInventory
from manager.models.rentinhand_order import ManagerRentInHandOrder
from product.models.bag.order import Order
from product.models.category import Category
from product.models.product import Product


def get_days(start_time, end_time):
    days = math.ceil((end_time - start_time).total_seconds() / (24 * 60 * 60))
    if (days == 0): 
        days = 1
    return days
    
class ManagerProductStat(models.Model):
    start_at = models.DateTimeField(null=True)
    end_at = models.DateTimeField(null=True)
    category = None

    products = None
    orders = None
    rnh_orders = None
    orders_requests = {}
    orders_approved = {}
    inventories = None

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        filter, rnh_filter = {}, {}
        
        if(self.start_at):
            filter.update({"created_at__gte": self.start_at})
            rnh_filter.update({"created_at__gte": self.start_at})
        else: 
            filter.update({"created_at__gte": now_minus_28()})
            rnh_filter.update({"created_at__gte": now_minus_28()})

        if(self.end_at):
            filter.update({"created_at__lte": self.end_at})
            rnh_filter.update({"created_at__lte": self.end_at})

        if(self.category):
            filter.update({"category_id": self.category.id})

        self.orders = Order.objects.filter(**filter)
        self.rnh_orders = ManagerRentInHandOrder.objects.filter(**rnh_filter)
        self.inventories = ManagerRentInHandInventory.objects.all()

        self.orders_requests, inventories, productIds = {}, [], []

        for productId, productRnhIds, count, start_time, end_time in (self.orders.values_list('bag__products__product', 'bag__products__product__rnh_ids', 'bag__products__count', 'start_time', 'end_time')):
            days = get_days(start_time, end_time)
            if(str(productId) in self.orders_requests.keys()):
                self.orders_requests.update({
                    str(productId): self.orders_requests[str(productId)] + days*count
                })
            else:
                self.orders_requests.update({
                    str(productId): days*count
                })
            productIds.append(productId)
            if(productRnhIds):
                inventories.extend(productRnhIds)

        self.products = Product.objects.filter(id__in=productIds)
        self.init_inventory_count()

    def init_inventory_count(self):
        self.orders_approved = {}
        rnh_inv = []
        for list, start_time, end_time in self.rnh_orders.values_list('inventories', 'start_time', 'end_time'):
            days = get_days(start_time, end_time)
            for item in list:
                rnh_inv.append((item, days))
                
        print(')000000(')
        for i in self.inventories.values_list('id', flat=True):
            print(i)
            self.orders_approved.update({str(i):0})
        print(')000000(')

        for inventory, days in rnh_inv:
            if(str(inventory) in self.orders_approved.keys()):
                self.orders_approved.update({
                    str(inventory): self.orders_approved[str(inventory)] + days
                })
            else:
                self.orders_approved.update({
                    str(inventory): days
                })

        self.orders_approved = {self.inventories.get(id=int(k)).rnh_id: int(v) for k, v in self.orders_approved.items()}
    
    class Meta: 
        managed = False