from rest_framework import serializers
from product.models.product import Product

class ManageProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"