from rest_framework import serializers
from product.models.category import Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name_ru', 'name_kk', 'icon', 'slug')