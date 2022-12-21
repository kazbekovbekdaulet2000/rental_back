from rest_framework import serializers
from manager.models.inventory.inventory_photo import InventoryPhoto



class InventoryPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = InventoryPhoto
        fields = ('id', 'photo')


class InventoryPhotoDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = InventoryPhoto
        fields = "__all__"
