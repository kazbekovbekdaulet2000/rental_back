from rest_framework import serializers
from common.image_progressive import create_thumbnail
from product.models.product_photo import ProductPhoto, ProductPhotoType


class ManagerProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductPhoto
        fields = ['id', 'product', 'image', 'image_thumb360', 'image_thumb720', 'image_thumb1080', 'type']
        read_only_fields = ['product', 'image_thumb360', 'image_thumb720', 'image_thumb1080']

    def create(self, validated_data):
        validated_data['product_id'] = self.context['view'].kwargs['id']
        return super().create(validated_data)


class ManagerServiceImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductPhoto
        fields = ['id', 'service', 'image', 'image_thumb360', 'image_thumb720', 'image_thumb1080', 'type']
        read_only_fields = ['image_thumb360', 'image_thumb720', 'image_thumb1080']

    def create(self, validated_data):
        validated_data['service_id'] = self.context['view'].kwargs['id']
        return super().create(validated_data)


class ManagerProductImageBulkCreateSerializer(serializers.Serializer):
    list = serializers.ListField(
        child=serializers.ImageField(),
        write_only=True,
        required=False
    )

    def create(self, validated_data):
        return super().create(validated_data)

    def create(self, validated_data):
        product_id = self.context['view'].kwargs['product_id']
        return ProductPhoto.objects.bulk_create([
            ProductPhoto(
                image=image,
                product_id=product_id,
                image_thumb1080=create_thumbnail(image, 1080),
                image_thumb720=create_thumbnail(image, 720),
                image_thumb360=create_thumbnail(image, 360),
                type=ProductPhotoType.CAROUSEL
            ) for image in validated_data.get('list')
        ])