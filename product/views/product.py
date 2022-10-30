from rest_framework import generics
from rest_framework import permissions
from product.models.product import Product
from product.serializers.product import BaseProductSerializer, ProductSerializer
from django_filters.rest_framework import DjangoFilterBackend
from product.utils import ProductCategoryFilter
from rest_framework.filters import SearchFilter
from django.shortcuts import get_object_or_404


class ProductList(generics.ListAPIView):
    queryset = Product.objects.filter(active=True).order_by('category', 'order', 'created_at')
    serializer_class = BaseProductSerializer
    permission_classes = (permissions.AllowAny, )
    filter_backends = (DjangoFilterBackend, SearchFilter)
    search_fields = (
        'name_ru', 'name_kk', 'tags',
        'category__name_kk', 'category__name_ru',
        'description_kk', 'description_ru'
    )
    filterset_class = ProductCategoryFilter


class ProductDetail(generics.RetrieveAPIView):
    lookup_field = 'slug'
    queryset = Product.objects.all().order_by('category', 'order', 'created_at')
    serializer_class = ProductSerializer
    permission_classes = (permissions.AllowAny, )


class ProductRelatedList(generics.ListAPIView):
    lookup_field = 'slug'
    serializer_class = BaseProductSerializer
    permission_classes = (permissions.AllowAny, )
    pagination_class = None
    
    def get_queryset(self):
        return Product.objects.filter(id__in=self.get_object().related_products_array).order_by('category', 'order', 'created_at')

    def get_object(self):
        queryset = Product.objects.filter(active=True).order_by('category', 'order', 'created_at')
        lookup_url_kwarg = self.lookup_url_kwarg or self.lookup_field
        filter_kwargs = {self.lookup_field: self.kwargs[lookup_url_kwarg]}
        obj = get_object_or_404(queryset, **filter_kwargs)
        self.check_object_permissions(self.request, obj)
        return obj