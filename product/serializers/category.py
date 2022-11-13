from rest_framework import serializers
from product.models.category import Category
from product.models.product import Product
from product.serializers.product_photo import ProductPhotoSerializer
from product.serializers.product_service import ProductServiceSerializer


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name_kk', 'name_ru', 'category', 'active', 'slug')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name_ru', 'name_kk', 'icon', 'slug')


class CategoryProductSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    services = serializers.SerializerMethodField()
    set_products = serializers.SerializerMethodField()

    def get_image(self, instance):
        images_instances = instance.images.filter(type=1)
        if (len(images_instances) > 0):
            return ProductPhotoSerializer(images_instances[0], many=False, context={"request": self.context['request']}).data
        return None

    def get_services(self, instance):
        return ProductServiceSerializer(instance.services.all(), many=True, context={"request": self.context['request']}).data

    def get_set_products(self, instance):
        if (instance.type != 0):
            products = Product.objects.filter(id__in=instance.set.filter(set_product__isnull=False).values_list('set_product', flat=True)).order_by('category', 'order', 'created_at')
            return ProductSerializer(products, context={"request": self.context['request']}, many=True).data
        return None

    class Meta:
        model = Product
        fields = ('id', 'name_kk', 'name_ru', 'type', 'daily_price',
                  'slug', 'image', 'services', 'set_products')


class AllCategoryProductSerializer(serializers.ModelSerializer):
    products = serializers.SerializerMethodField()

    def get_products(self, obj):
        return CategoryProductSerializer(obj.products.filter(active=True), context={"request": self.context['request']}, many=True).data

    class Meta:
        model = Category
        fields = ('id', 'name_ru', 'name_kk', 'icon', 'slug', 'products')
