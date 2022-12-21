from rest_framework import serializers
from common.image_progressive import create_thumbnail
from manager.serializers.inventory.inventory import InventorySerializer
from manager.serializers.inventory.inventory_tarif import InventoryTarifSerializer
from product.models.product import Product
from product.models.product_photo import ProductPhoto
from product.serializers.product_photo import ProductPhotoSerializer


class BaseManagerProductSerializer(serializers.ModelSerializer):
    image = ProductPhotoSerializer(many=False)
    tarif = InventoryTarifSerializer(many=False)
    
    class Meta:
        model = Product
        fields = ['id', 'slug', 'name_ru', 'name_kk', 'order', 'articule', 'description_ru', 'description_kk',
                  'daily_price', 'tags', 'category', 'type', 'related_products_array', 'image', 'tarif']


class ManagerProductSerializer(serializers.ModelSerializer):
    images = ProductPhotoSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ['name_ru', 'name_kk', 'order', 'articule', 'description_ru', 'description_kk',
                  'daily_price', 'tags', 'category', 'instruction_video', 'amount', 'active',
                  'type', 'related_products_array', 'images', 'parts']


class ManagerProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class ManagerProductCreateSerializer(serializers.ModelSerializer):
    image_list = serializers.ListField(
        child=serializers.ImageField(),
        write_only=True,
        required=False
    )
    main_image = serializers.ImageField(required=False)

    class Meta:
        model = Product
        fields = ['name_ru', 'name_kk', 'order', 'articule', 'description_ru', 'description_kk',
                  'daily_price', 'tags', 'category', 'instruction_video', 'amount', 'active',
                  'type', 'related_products_array', 'main_image', 'image_list']

    def create(self, validated_data):
        try:
            images = validated_data.pop('image_list')
        except:
            images = []

        try:
            main_image = validated_data.pop('main_image')
        except:
            main_image = None

        product = super().create(validated_data)

        ProductPhoto.objects.bulk_create(
            ProductPhoto(
                image=image,
                product=product,
                image_thumb1080=create_thumbnail(image, 1080),
                image_thumb720=create_thumbnail(image, 1080),
                image_thumb360=create_thumbnail(image, 720)
            ) for image in images
        )

        if (main_image):
            ProductPhoto.objects.create(
                image=main_image, product=product, type=1)

        return product
