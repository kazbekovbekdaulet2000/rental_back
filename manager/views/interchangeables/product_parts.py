from rest_framework import generics
from rest_framework import permissions
from manager.serializers.inventory.product_part import ManagerProductPartSerializer
from product.models.product_part import ProductPart


class ManagerProductInterchangeableList(generics.ListCreateAPIView):
    queryset = ProductPart.objects.all()
    serializer_class = ManagerProductPartSerializer
    permission_classes = (permissions.IsAuthenticated, )
    pagination_class = None

    def get_queryset(self):
        return ProductPart.objects.filter(product_id=self.kwargs['product_id'])


class ManagerProductInterchangeableDetail(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = "id"
    serializer_class = ManagerProductPartSerializer
    permission_classes = (permissions.IsAuthenticated, )

    def get_queryset(self):
        return ProductPart.objects.filter(product_id=self.kwargs['product_id'])
