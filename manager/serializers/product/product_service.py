from product.models.product_service import ProductService
from rest_framework import serializers


class ManagerProductServiceCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductService
        fields = ('service', 'required')
    
    def create(self, validated_data):
        validated_data['product'] = self.context['view'].kwargs['id']
        return super().create(validated_data)