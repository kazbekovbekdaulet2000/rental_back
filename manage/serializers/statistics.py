from rest_framework import serializers
from manage.models.stats import Statistics
from manage.serializers.order import ManageOrderSerializer


class ManageStatisticsSerializer(serializers.ModelSerializer):
    # approved_orders = ManageOrderSerializer(many=True)

    class Meta:
        model = Statistics
        fields = ['orders_count', 'rnh_orders_count', 'products_value', 'services_value', 'total_days_count', 'rnh_days_count']
