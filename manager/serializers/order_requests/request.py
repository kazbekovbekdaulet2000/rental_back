from rest_framework import serializers
from manager.models.order_request.request import OrderRequest
from manager.serializers.client.client import BaseClientSerializer
from manager.serializers.order_requests.request_inventory import OrderRequestInventorySerializer


class OrderRequestSerializer(serializers.ModelSerializer):
    client = BaseClientSerializer(many=False)
    inventories = OrderRequestInventorySerializer(many=True)

    class Meta:
        model = OrderRequest
        fields = "__all__"


class OrderRequestCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderRequest
        fields = "__all__"
