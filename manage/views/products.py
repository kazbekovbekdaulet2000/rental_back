from rest_framework import generics
from rest_framework import permissions
from manage.serializers.product import ManageProductSerializer
from product.models.product import Product
from django_filters.rest_framework import DjangoFilterBackend
from product.utils import ProductCategoryFilter
from rest_framework.filters import SearchFilter


class ManageProductList(generics.ListAPIView):
    queryset = Product.objects.filter().order_by('category', 'order', 'created_at')
    serializer_class = ManageProductSerializer
    permission_classes = (permissions.IsAuthenticated, )
    filter_backends = (DjangoFilterBackend, SearchFilter)
    search_fields = ('name_ru', 'name_kk', 'tags')
    filterset_class = ProductCategoryFilter


class ManageProductDetail(generics.RetrieveAPIView):
    lookup_field = 'id'
    queryset = Product.objects.filter()
    serializer_class = ManageProductSerializer
    permission_classes = (permissions.IsAuthenticated, )
