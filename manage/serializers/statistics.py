from rest_framework import serializers
from manage.models.stats import Statistics
from manage.serializers.order import ManageOrderSerializer


class ManageStatisticsSerializer(serializers.ModelSerializer):
    approved_orders = ManageOrderSerializer(many=True)

    class Meta:
        model = Statistics
        fields = ['approved_orders', 'approved_orders_count', 'orders_count', 'products_value', 'services_value', 'total_days_count', 'approved_days_count']
