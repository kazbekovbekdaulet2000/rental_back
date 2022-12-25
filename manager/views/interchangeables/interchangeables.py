from rest_framework import generics
from rest_framework import permissions
from manager.models.interchangeable.interchangeable import Interchangeable
from manager.serializers.product_parts.product_parts import InterchangeableCreateSerializer, InterchangeableSerializer
from rest_framework.filters import SearchFilter


class ManagerInterchangeableList(generics.ListCreateAPIView):
    queryset = Interchangeable.objects.all()
    serializer_class = InterchangeableSerializer
    permission_classes = (permissions.IsAuthenticated, )
    filter_backends = (SearchFilter, )
    search_fields = ('name', 'inventories__name')

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return InterchangeableCreateSerializer
        return super().get_serializer_class()


class ManagerInterchangeableDetail(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = "id"
    queryset = Interchangeable.objects.all()
    serializer_class = InterchangeableSerializer
    permission_classes = (permissions.IsAuthenticated, )
