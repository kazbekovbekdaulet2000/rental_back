from rest_framework import serializers
from product.models.bag.bag_product import UserBagItem
from product.models.service import Service
from product.serializers.product import BaseProductSerializer
from product.models.bag.bag import UserBag
from product.serializers.product_service import ServiceSerializer


class UserBagItemSerializer(serializers.ModelSerializer):
    product = BaseProductSerializer(read_only=True)

    class Meta:
        model = UserBagItem
        fields = ('id', 'product', 'count')


class UserBagItemCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserBagItem
        fields = ('id', 'product', 'count')

    def validate(self, attrs):
        if (self.context['request'].method == "POST"):
            product_id = attrs['product'].id
        else:
            product_id = self.context['view'].kwargs['id']
        if (UserBagItem.objects.filter(
            order_id=self.context['view'].kwargs['uuid'],
            product_id=product_id
        ).exists()):
            raise serializers.ValidationError({'product': 'already exists'})
        return super().validate(attrs)

    def create(self, validated_data):
        validated_data['order_id'] = self.context['view'].kwargs['uuid']
        return super().create(validated_data)


class UserBagSerializer(serializers.ModelSerializer):
    products = UserBagItemSerializer(many=True)
    services = serializers.SerializerMethodField(read_only=True)

    def get_services(self, obj):
        return ServiceSerializer(
            Service.objects.filter(id__in=obj.products.values_list('product__services__service', flat=True)), 
            many=True,
            context={"request": self.context['request']}
        ).data

    class Meta:
        model = UserBag
        fields = ('id', 'products', 'total_price', 'services', 'services_price', 'products_price', 'delivery', 'delivery_price')


class UserBagCreateSerializer(serializers.ModelSerializer):
    products = UserBagItemSerializer(many=True, read_only=True)

    class Meta:
        model = UserBag
        fields = ('id', 'delivery', 'previous_order', 'products')
