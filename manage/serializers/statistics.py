from rest_framework import serializers
from manage.models.stats import Statistics
from manage.serializers.order import ManageOrderSerializer
from manage.serializers.product import ManageProductSerializer


class ManageStatisticsSerializer(serializers.ModelSerializer):
    # products = ManageProductSerializer(many=True)
    approved_orders = ManageOrderSerializer(many=True)

    class Meta:
        model = Statistics
        fields = ['approved_orders', 'approved_orders_count', 'orders_count', 'products_value', 'services_value', 'days_count', 'approved_days_count']
