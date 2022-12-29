from rest_framework import serializers
from common.image_progressive import create_thumbnail
from manager.models.inventory.inventory_photo import InventoryPhoto


class InventoryPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = InventoryPhoto
        fields = ('id', 'photo')


class InventoryPhotoDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = InventoryPhoto
        fields = "__all__"


class InventoryPhotoBulkCreate(serializers.Serializer):
    list = serializers.ListField(
        child=serializers.ImageField(),
        required=False
    )

    def create(self, validated_data):
        inventory_id = self.context['view'].kwargs['inventory_id']
        return InventoryPhoto.objects.bulk_create([
            InventoryPhoto(
                photo=create_thumbnail(file, 720),
                inventory_id=inventory_id
            ) for file in validated_data.get('list')
        ])
