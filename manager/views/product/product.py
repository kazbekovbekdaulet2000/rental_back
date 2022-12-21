from rest_framework import generics
from rest_framework import permissions
from manager.serializers.product.product import (
    BaseManagerProductSerializer,
    ManagerProductCreateSerializer,
    ManagerProductSerializer
)
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
        if self.request.method == "GET":
            return super().get_serializer_class()
        return ManagerProductCreateSerializer
