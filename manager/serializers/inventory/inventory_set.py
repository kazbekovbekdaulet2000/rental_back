from rest_framework import serializers
from manager.models.inventory.inventory_set import InventorySet, InventorySetItem
from manager.serializers.product_parts.product_parts import InterchangeableSerializer


class InventorySetItemSerializer(serializers.ModelSerializer):
    interchangeable = InterchangeableSerializer(many=False, read_only=True)

    class Meta:
        model = InventorySetItem
        fields = ('id', 'set', 'interchangeable', 'count')


class InventorySetItemCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = InventorySetItem
        fields = ('id', 'set', 'interchangeable', 'count')


class InventorySetSerializer(serializers.ModelSerializer):
    items = InventorySetItemSerializer(many=True, read_only=True)

    class Meta:
        model = InventorySet
        fields = ('id', 'name', 'items')
