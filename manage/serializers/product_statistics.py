from rest_framework import serializers
from manage.models.stats_product_count import ProductCountStatistics
from product.models.product import Product


class ManagerProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name_ru', 'name_kk', 'articule', 'daily_price', 'category', 'slug', 'type')


class ManagerProductStatisticsSerializer(serializers.ModelSerializer):
    product = ManagerProductSerializer()
    class Meta:
        model = ProductCountStatistics
        fields = ('product', 'total_days_count', 'total_orders_count', 'money_amount')
