from manager.serializers.order_requests.request import OrderRequestSerializer
from rest_framework import generics
from rest_framework import permissions
from manager.models.order_request.request import OrderRequest


class OrderRequestList(generics.ListCreateAPIView):
    queryset = OrderRequest.objects.all()
    serializer_class = OrderRequestSerializer
    permission_classes = (permissions.IsAuthenticated, )


class OrderRequestDetail(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'
    queryset = OrderRequest.objects.all()
    serializer_class = OrderRequestSerializer
    permission_classes = (permissions.IsAuthenticated, )
