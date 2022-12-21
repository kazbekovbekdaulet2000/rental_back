from rest_framework import generics
from rest_framework import permissions
from manager.serializers.product.product_image import ManagerProductImageSerializer
from product.models.product_photo import ProductPhoto


class ManagerProductImageList(generics.ListCreateAPIView):
    queryset = None
    serializer_class = ManagerProductImageSerializer
    permission_classes = (permissions.IsAuthenticated, )
    pagination_class = None

    def get_queryset(self):
        return ProductPhoto.objects.filter(product_id=self.kwargs['id'])


class ManagerProductImageDelete(generics.DestroyAPIView):
    lookup_field = 'id'
    queryset = None
    serializer_class = ManagerProductImageSerializer
    permission_classes = (permissions.IsAuthenticated, )

    def get_queryset(self):
        return ProductPhoto.objects.filter(product_id=self.kwargs['product_id'])
