from rest_framework import generics
from rest_framework import permissions
from manager.serializers.product.product_set import (
    ManagerProductSetCreateSerializer,
    ManagerProductSetSerializer
)
from product.models.product_set import ProductSet


# class ManagerProductServiceList(generics.ListAPIView):
#     queryset = None
#     serializer_class = ManagerProductSetSerializer
#     permission_classes = (permissions.IsAuthenticated, )
#     pagination_class = None

#     def get_queryset(self):
#         return ProductService.objects.filter(product_id=self.kwargs['id'])

#     def get_serializer_class(self):
#         return super().get_serializer_class()


# class ManagerProductSetDetail(generics.RetrieveUpdateDestroyAPIView):
#     lookup_field = 'id'
#     queryset = None
#     serializer_class = ManagerProductSetSerializer
#     permission_classes = (permissions.IsAuthenticated, )

#     def get_queryset(self):
#         return ProductSet.objects.filter(product_id=self.kwargs['product_id'])

#     def get_serializer_class(self):
#         if self.request.method in permissions.SAFE_METHODS:
#             return super().get_serializer_class()
#         return ManagerProductSetCreateSerializer
