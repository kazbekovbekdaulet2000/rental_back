from manager.models.inventory.inventory import Inventory
from rest_framework import serializers
from manager.models.inventory.inventory_photo import InventoryPhoto
from manager.serializers.inventory.inventory_image import InventoryPhotoSerializer
from manager.serializers.inventory.inventory_tarif import InventoryTarifSerializer


class InventorySerializer(serializers.ModelSerializer):
    photos = InventoryPhotoSerializer(many=True)
    default_tarif = InventoryTarifSerializer(many=False)

    class Meta:
        model = Inventory
        fields = "__all__"


class InventoryCreateSerializer(serializers.ModelSerializer):
    photos = serializers.ListField(
        child=serializers.ImageField(),
        required=False
    )

    class Meta:
        model = Inventory
        fields = ('id', 'name', 'unique_id', 'status', 'buy_price', 
                  'buy_date', 'comment', 'photos', 'rent_point', 'category')

    def create(self, validated_data):
        photos = validated_data.get('photos') or []
        dict = {}
        for val in list(validated_data):
            if (not (str(val) == 'photos')):
                dict.update({str(val): validated_data.get(val)})

        inventory = Inventory.objects.create(**dict)

        InventoryPhoto.objects.bulk_create(
            InventoryPhoto(photo=photo, inventory=inventory) for photo in photos
        )

        return validated_data


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
