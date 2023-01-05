from rest_framework import serializers
from manager.models.inventory.inventory_set import InventorySet, InventorySetItem
from manager.models.inventory.inventory_tarif import InventoryTarif
from manager.serializers.product_parts.product_parts import InterchangeableSerializer


class InventorySetItemSerializer(serializers.ModelSerializer):
    interchangeable = InterchangeableSerializer(many=False, read_only=True)

    class Meta:
        model = InventorySetItem
        fields = ('id', 'set', 'interchangeable', 'tarif_price', 'count')


class InventorySetItemCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = InventorySetItem
        fields = ('id', 'set', 'interchangeable', 'tarif_price', 'count')

    def create(self, validated_data):
        interchangeable = validated_data['interchangeable']
        inventories = interchangeable.inventories.all()
        if (inventories.count() < validated_data['count']):
            raise serializers.ValidationError(
                {'CountError': 'Недостаточно инвентарей'})
        price = validated_data['tarif_price']
        set_item = super().create(validated_data)

        # creating tarifs for set id
        InventoryTarif.objects.bulk_create([
            InventoryTarif(
                name=f"interchangeable_{interchangeable.id}",
                inventory_id=inventory.id,
                inventory_set_id=set_item.id,
                price=price
            ) for inventory in inventories
        ])

        return set_item


class InventorySetSerializer(serializers.ModelSerializer):
    items = InventorySetItemSerializer(many=True, read_only=True)
    overall_price = serializers.SerializerMethodField()

    def get_overall_price(self, obj):
        sum = 0
        for i, j in obj.items.all().values_list('count', 'tarif_price'):
            sum += i * j
        return sum

    class Meta:
        model = InventorySet
        fields = ('id', 'name', 'items', 'unique_id', 'category', 'overall_price')
