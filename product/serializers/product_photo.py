from rest_framework import serializers
from product.models.product_photo import ProductPhoto


class ProductPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductPhoto
        fields = ('id', 'image', 'image_thumb360',
                  'image_thumb720', 'image_thumb1080', 'type')


class ProductPhotoCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductPhoto
        fields = ('image', 'type')
        required_fields = ('image', 'type')
