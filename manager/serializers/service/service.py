from rest_framework import serializers
from common.image_progressive import create_thumbnail
from product.models.product_photo import ProductPhoto
from product.models.service import Service
from product.serializers.product_photo import ProductPhotoSerializer


class ManagerServiceSerializer(serializers.ModelSerializer):
    image_list = serializers.ListField(
        child=serializers.ImageField(),
        write_only=True,
        required=False
    )
    main_image = serializers.ImageField(required=False)
    image = serializers.SerializerMethodField()

    def get_image(self, instance):
        images_instances = instance.images.filter(type=1)
        if (len(images_instances) > 0):
            return ProductPhotoSerializer(images_instances[0], many=False, context={"request": self.context['request']}).data
        return None

    class Meta:
        model = Service
        fields = ['id', 'name_ru', 'name_kk', 'description_ru', 'description_kk',
                  'daily_price', 'tags', 'active', 'main_image', 'image_list', 'image']

    def create(self, validated_data):
        try:
            image_list = validated_data.pop('image_list')
        except:
            image_list = []

        try:
            main_image = validated_data.pop('main_image')
        except:
            main_image = None

        service = super().create(validated_data)

        ProductPhoto.objects.bulk_create(
            ProductPhoto(
                image=image,
                service=service,
                image_thumb1080=create_thumbnail(image, 1080),
                image_thumb720=create_thumbnail(image, 1080),
                image_thumb360=create_thumbnail(image, 720)
            ) for image in image_list
        )
        if (main_image):
            ProductPhoto.objects.create(
                image=main_image, service=service, type=1)

        return service


class ManagerServiceDetailSerializer(serializers.ModelSerializer):
    images = ProductPhotoSerializer(many=True)

    class Meta:
        model = Service
        fields = "__all__"
