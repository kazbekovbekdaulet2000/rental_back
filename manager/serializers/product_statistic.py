from rest_framework import serializers
from manager.models.statistics.product_statistic import ManagerProductStat
from product.models.product import Product


class ManagerProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name_kk', 'name_ru', 'category', 'type', 'active', 'daily_price', 'slug', 'articule', 'rnh_ids')


class ManagerProductStatSerializer(serializers.HyperlinkedModelSerializer):
    products = serializers.SerializerMethodField()

    def get_products(self, obj):
        return ManagerProductSerializer(obj.products, many=True).data

    class Meta:
        model = ManagerProductStat
        fields = ['products', 'orders_requests', 'orders_approved']