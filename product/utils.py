from django_filters import rest_framework as filters
from product.models.product import Product

class ProductCategoryFilter(filters.FilterSet):
    class Meta:
        model = Product
        fields = ['category__slug',]