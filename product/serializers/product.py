from django.shortcuts import get_object_or_404
from rest_framework import serializers
from product.models.product import Product
from product.serializers.category import CategorySerializer
from product.serializers.eav import ValueSerializer
from product.serializers.product_photo import ProductPhotoSerializer
from product.serializers.product_service import ProductServiceSerializer


class BaseProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many=False) 
    image = serializers.SerializerMethodField()
    services = serializers.SerializerMethodField(read_only=True)

    def get_image(self, instance):
        images_instances = instance.images.filter(type=1)
        if(len(images_instances) > 0):
            return ProductPhotoSerializer(images_instances[0], many=False, context={"request": self.context['request']}).data
        return None

    def get_services(self, instance):
        return instance.services.values_list('service__id', flat=True)

    class Meta:
        model = Product
        fields = ('id', 'name_kk', 'name_ru', 'category',
                  'daily_price', 'slug', 'articule', 'image', 'amount', 'services', 'child_products')


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many=False)
    images = serializers.SerializerMethodField()
    child_products = BaseProductSerializer(many=True)
    specs = serializers.SerializerMethodField()
    services = ProductServiceSerializer(read_only=True)

    def get_specs(self, obj):
        return ValueSerializer(obj.eav.select_related('attribute', 'product'), many=True).data

    def get_images(self, instance):
        images_instances = instance.images.filter(type=0)
        return ProductPhotoSerializer(images_instances, many=True, context={"request": self.context['request']}).data

    class Meta:
        model = Product
        exclude = ('related_products', 'parent_product')
