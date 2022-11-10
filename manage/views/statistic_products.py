import math
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import permissions
from manage.models.rentinhand_inventory import RentInHandInventory
from manage.models.rentinhand_order import RentInHandOrder
from manage.models.stats_product import ProductStatistics
from manage.permissions import IsStatisticManager
from manage.serializers.product_statistics import ManagerProductStatisticsSerializer
from datetime import datetime, timedelta


def now_minus_30(): return datetime.now() - timedelta(days=28)


class ManageStatisticProducts(generics.ListAPIView):
    serializer_class = ManagerProductStatisticsSerializer
    # permission_classes = (permissions.IsAuthenticated, IsStatisticManager)
    product_stat = None
    pagination_class = None

    def get_queryparams(self):
        return self.request.query_params

    def get_queryset(self):
        params = self.request.query_params
        self.product_stat = ProductStatistics(start_at=params.get('start_at'), end_at=params.get('end_at'))
        return self.product_stat.product_count
    
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        data = serializer.data
        data = sorted(data, key = lambda i: -i['total_orders_count'])
        return Response(data)


class ManageStatisticProductsRNH(generics.ListAPIView):
    # permission_classes = (permissions.IsAuthenticated, IsStatisticManager)
    product_stat = None
    pagination_class = None

    def get_queryparams(self):
        return self.request.query_params

    def list(self, request, *args, **kwargs):
        params = self.request.query_params
        filter = {}
        if (params.get('start_at')):
            filter.update({"start_time__gte": params.get('start_at')})
        else:
            filter.update({"start_time__gte": now_minus_30()})

        if (params.get('end_at')):
            filter.update({"end_time__lte": params.get('end_at')})

        ids = []
        inventory_name = {}
        inventory_days = {}
        orders = RentInHandOrder.objects.filter(**filter)

        for inventories in orders.values_list('inventories'):
            for i in inventories[0]:
                ids.append(i)

        inventories = RentInHandInventory.objects.filter(id__in=ids)

        for inventory in inventories:
            inventory_name.update({str(inventory.id): inventory.title})

        for order in orders:
            days = self.get_days(order.start_time, order.end_time)
            for i in order.inventories:
                inventory = inventory_name[str(i)]
                if inventory in inventory_days.keys():
                    inventory_days.update({inventory: {"count": inventory_days.get(inventory)['count'] + 1, "days": inventory_days.get(inventory)['days'] + days}})
                else:
                    inventory_days.update({inventory: {"count": 1, "days": days}})

        inventory_days = {k: v for k, v in sorted(inventory_days.items(), key=lambda item: -item[1]['count'])}

        return Response(inventory_days)

    def get_days(self, start_time, end_time):
        days = math.ceil((end_time - start_time).total_seconds() / (24 * 60 * 60))
        if (days == 0): 
            days = 1
        return days