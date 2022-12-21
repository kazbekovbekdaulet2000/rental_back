from rest_framework import serializers
from product.models.product_photo import ProductPhoto


class ManagerProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductPhoto
        fields = ['id', 'product', 'image', 'image_thumb360',
                  'image_thumb720', 'image_thumb1080', 'type']
        read_only_fields = ['product', 'image_thumb360',
                            'image_thumb720', 'image_thumb1080']

    def create(self, validated_data):
        validated_data['product_id'] = self.context['view'].kwargs['id']
        return super().create(validated_data)


class ManagerServiceImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductPhoto
        fields = ['id', 'service', 'image', 'image_thumb360',
                  'image_thumb720', 'image_thumb1080', 'type']
        read_only_fields = ['image_thumb360',
                            'image_thumb720', 'image_thumb1080']

    def create(self, validated_data):
        validated_data['service_id'] = self.context['view'].kwargs['id']
        return super().create(validated_data)
