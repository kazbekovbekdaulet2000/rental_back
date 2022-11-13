from rest_framework import serializers
from manager.models.statistics.statistic import ManagerStat


class ManagerStatSerializer(serializers.ModelSerializer):
    class Meta:
        model = ManagerStat
        fields = ['orders_count', 'rnh_orders_count', 'orders_price', 'rnh_orders_price']