from rest_framework import serializers
from product.models.product_photo import ProductPhoto


class ProductPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductPhoto
        fields = "__all__"