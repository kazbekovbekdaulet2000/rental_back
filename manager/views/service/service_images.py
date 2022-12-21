from rest_framework import generics
from rest_framework import permissions
from manager.serializers.product.product_image import ManagerServiceImageSerializer
from product.models.product_photo import ProductPhoto


class ManagerServiceImageList(generics.ListCreateAPIView):
    queryset = None
    serializer_class = ManagerServiceImageSerializer
    permission_classes = (permissions.IsAuthenticated, )
    pagination_class = None

    def get_queryset(self):
        return ProductPhoto.objects.filter(service_id=self.kwargs['id'])


class ManagerServiceImageDelete(generics.DestroyAPIView):
    lookup_field = 'id'
    queryset = None
    serializer_class = ManagerServiceImageSerializer
    permission_classes = (permissions.IsAuthenticated, )

    def get_queryset(self):
        return ProductPhoto.objects.filter(service_id=self.kwargs['service_id'])
