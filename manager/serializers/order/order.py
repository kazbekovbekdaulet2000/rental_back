from rest_framework import serializers
from product.models.bag.order import Order


class ManagerOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"
