from manager.serializers.order_requests.request import OrderRequestCreateSerializer, OrderRequestSerializer
from rest_framework import generics
from rest_framework import permissions
from manager.models.order_request.request import OrderRequest
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend


class OrderRequestList(generics.ListCreateAPIView):
    queryset = OrderRequest.objects.all()
    serializer_class = OrderRequestSerializer
    permission_classes = (permissions.IsAuthenticated, )
    filter_backends = (DjangoFilterBackend, )
    filterset_fields = ('status', )

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return OrderRequestCreateSerializer
        return super().get_serializer_class()


class OrderRequestDetail(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'
    queryset = OrderRequest.objects.all()
    serializer_class = OrderRequestSerializer
    permission_classes = (permissions.IsAuthenticated, )
