from rest_framework import serializers
from product.models.product_part import ProductPart


class ManagerProductPartSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductPart
        fields = "__all__"
