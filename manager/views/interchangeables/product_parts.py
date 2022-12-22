from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework import permissions
from manager.models.interchangeable.interchangeable import Interchangeable
from manager.serializers.product_parts.product_parts import InterchangeableSerializer
from product.models.product import Product


class ManagerProductPartList(generics.ListCreateAPIView):
    queryset = Interchangeable.objects.all()
    serializer_class = InterchangeableSerializer
    permission_classes = (permissions.IsAuthenticated, )
    pagination_class = None

    def get_queryset(self):
        product = get_object_or_404(Product, id=self.kwargs['product_id'])
        return product.parts


class ManagerProductPartDetail(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = "id"
    serializer_class = InterchangeableSerializer
    permission_classes = (permissions.IsAuthenticated, )

    def get_queryset(self):
        product = get_object_or_404(Product, id=self.kwargs['product_id'])
        return product.parts