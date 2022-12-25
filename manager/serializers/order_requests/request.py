from rest_framework import serializers
from manager.models.order_request.request import OrderRequest


class OrderRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderRequest
        fields = "__all__"