from rest_framework import serializers
from product.models.product_service import ProductService
from product.models.service import Service
from product.serializers.product_photo import ProductPhotoSerializer


class ServiceSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    def get_image(self, instance):
        images_instances = instance.images.filter(type=1)
        if(len(images_instances) > 0):
            return ProductPhotoSerializer(images_instances[0], many=False, context={"request": self.context['request']}).data
        return None

    class Meta:
        model = Service
        fields = "__all__"


class ProductServiceSerializer(serializers.ModelSerializer):
    service = serializers.SerializerMethodField()

    def get_service(self, instance):
        return ServiceSerializer(instance.service, many=False, context={"request": self.context['request']}).data

    class Meta:
        model = ProductService
        exclude = ('product',)
