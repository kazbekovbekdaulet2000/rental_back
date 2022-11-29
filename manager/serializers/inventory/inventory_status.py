from rest_framework import serializers
from manager.models.inventory.inventory_status import InventoryStatus


class InventoryStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = InventoryStatus
        fields = "__all__"
