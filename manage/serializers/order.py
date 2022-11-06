from rest_framework import serializers
from product.models.bag.order import Order


class ManageOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('id', 'name', 'phone', 'first_time_order', 'start_time', 'end_time', 'comment', 'products_price', 'services_price', 'total_price', 'bag')
        read_only_fields = ( 'products_price', 'services_price', 'total_price', 'bag')