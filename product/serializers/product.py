from rest_framework import serializers
from product.models.product import Product
from product.serializers.category import CategorySerializer
from product.serializers.eav import ValueSerializer
from product.serializers.product_photo import ProductPhotoSerializer
from product.serializers.product_service import ProductServiceSerializer


class BaseMinProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many=False)
    class Meta:
        model = Product
        fields = ('id', 'name_kk', 'name_ru', 'category', 'slug')


class BaseProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many=False)
    image = serializers.SerializerMethodField()
    services = serializers.SerializerMethodField(read_only=True)

    def get_image(self, instance):
        images_instances = instance.images.filter(type=1)
        if (len(images_instances) > 0):
            return ProductPhotoSerializer(images_instances[0], many=False, context={"request": self.context['request']}).data
        return None

    def get_services(self, instance):
        return instance.services.values_list('service__id', flat=True)

    class Meta:
        model = Product
        fields = ('id', 'name_kk', 'name_ru', 'category', 'type',
                  'daily_price', 'slug', 'articule', 'image', 'amount', 'services')


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many=False)
    images = serializers.SerializerMethodField()
    specs = serializers.SerializerMethodField()
    services = serializers.SerializerMethodField()
    set_products = serializers.SerializerMethodField()

    def get_specs(self, obj):
        return ValueSerializer(obj.eav.select_related('attribute', 'product'), many=True).data

    def get_images(self, instance):
        images_instances = instance.images.filter(type=0)
        return ProductPhotoSerializer(images_instances, many=True, context={"request": self.context['request']}).data

    def get_services(self, instance):
        return ProductServiceSerializer(instance.services.all(), many=True, context={"request": self.context['request']}).data

    def get_set_products(self, instance):
        if (instance.type != 0):
            products = Product.objects.filter(id__in = instance.set.filter(set_product__isnull=False).order_by('category', 'order', 'created_at').values_list('set_product', flat=True))
            return BaseMinProductSerializer(products, many=True, context={"request": self.context['request']}).data
        return None

    class Meta:
        model = Product
        exclude = ('related_products', )
