from rest_framework import generics
from rest_framework import permissions
from manager.serializers.product.product import (
    BaseManagerProductSerializer,
    ManagerProductCreateSerializer,
    ManagerProductSerializer,
    ManagerProductUpdateSerializer
)
from django.shortcuts import get_object_or_404
from product.models.product import Product
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend


class ManagerProductsList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = BaseManagerProductSerializer
    permission_classes = (permissions.IsAuthenticated, )
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filterset_fields = ['category', 'type', 'active']
    search_fields = ('name_kk', 'name_ru')

    def get_serializer_class(self):
        if self.request.method == "POST":
            return ManagerProductCreateSerializer
        return super().get_serializer_class()


class ManagerProductDetail(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'
    queryset = Product.objects.all()
    serializer_class = ManagerProductSerializer
    permission_classes = (permissions.IsAuthenticated, )

    def get_serializer_class(self):
        if self.request.method == "POST":
            return ManagerProductCreateSerializer
        if self.request.method in ['PATCH', 'PUT']:
            return ManagerProductUpdateSerializer
        return super().get_serializer_class()


class ManagerProductRelatedList(generics.ListAPIView):
    serializer_class = BaseManagerProductSerializer
    permission_classes = (permissions.IsAuthenticated, )
    pagination_class = None

    def get_object(self):
        obj = get_object_or_404(Product, id=self.kwargs['product_id'])
        self.check_object_permissions(self.request, obj)
        return obj

    def get_queryset(self):
        product = self.get_object()
        return Product.objects.filter(id__in=product.related_products_array)
