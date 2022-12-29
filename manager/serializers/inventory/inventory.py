from manager.models.inventory.inventory import Inventory
from rest_framework import serializers
from manager.serializers.inventory.inventory_image import InventoryPhotoSerializer
from manager.serializers.inventory.inventory_tarif import InventoryTarifSerializer


class InventorySerializer(serializers.ModelSerializer):
    photos = InventoryPhotoSerializer(many=True)
    default_tarif = InventoryTarifSerializer(many=False)

    class Meta:
        model = Inventory
        fields = "__all__"


class InventoryCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = ('id', 'name', 'unique_id', 'status', 'buy_price', 
                  'buy_date', 'comment', 'rent_point', 'category')
        read_only_fields = ('unique_id',)

    def create(self, validated_data):
        last_inventory=Inventory.objects.filter(category=validated_data.get('category')).count()
        id = last_inventory + 1
        validated_data['unique_id'] = validated_data.get('category').prefix + f"{id:04}"
        return super().create(validated_data)


class InventoryUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = ('id', 'name', 'unique_id', 'status', 'buy_price', 
                  'buy_date', 'comment', 'rent_point', 'category')


class ManagerInventoryBulkCreateItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = "__all__"


class ManagerInventoryBulkCreateSerializer(serializers.Serializer):
    list = ManagerInventoryBulkCreateItemSerializer(many=True, write_only=True)

    def create(self, validated_data):
        return Inventory.objects.bulk_create([
            Inventory(**obj) for obj in validated_data.get('list')
        ])
