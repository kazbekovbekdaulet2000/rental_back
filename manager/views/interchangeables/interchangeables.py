from rest_framework import generics
from rest_framework import permissions
from manager.models.interchangeable.interchangeable import Interchangeable
from manager.serializers.product_parts.product_parts import ManagerProductPartSerializer
from product.models.product import Product


class ManagerInterchangeableList(generics.ListCreateAPIView):
    queryset = Interchangeable.objects.all()
    serializer_class = ManagerProductPartSerializer
    permission_classes = (permissions.IsAuthenticated, )
    # filter_backends = (DjangoFilterBackend, SearchFilter)
    # search_fields = ('name', 'unique_id')
    # filterset_fields = ('category', 'status')
    
    pagination_class = None


class ManagerInterchangeableDetail(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = "id"
    queryset = Interchangeable.objects.all()
    serializer_class = ManagerProductPartSerializer
    permission_classes = (permissions.IsAuthenticated, )