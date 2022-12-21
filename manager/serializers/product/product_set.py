from manager.serializers.product.product import BaseManagerProductSerializer
from product.models.product_set import ProductSet
from rest_framework import serializers


class ManagerProductSetSerializer(serializers.ModelSerializer):
    set_product = BaseManagerProductSerializer(read_only=True)

    class Meta:
        model = ProductSet
        fields = ('id', 'set_product', 'count')


class ManagerProductSetCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductSet
        fields = ('id', 'set_product', 'count')

    def create(self, validated_data):
        validated_data['product'] = self.context['view'].kwargs['id']
        return super().create(validated_data)


class ManagerProductSetBulkCreateSerializer(serializers.Serializer):
    list = ManagerProductSetCreateSerializer(many=True, write_only=True)

    def create(self, validated_data):
        product_id = self.context['view'].kwargs['id']
        list = ProductSet.objects.bulk_create([
            ProductSet(product_id=product_id, set_product=obj['set_product'], count=obj['count']) for obj in validated_data.get('list')
        ])
        return list
