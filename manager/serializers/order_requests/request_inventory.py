from rest_framework import serializers
from manager.models.order_request.request_inventory import OrderRequestInventory
from manager.serializers.inventory.inventory import BaseInventorySerializer


class OrderRequestInventorySerializer(serializers.ModelSerializer):
    inventory = BaseInventorySerializer()

    class Meta:
        model = OrderRequestInventory
        fields = "__all__"
