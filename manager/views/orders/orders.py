from rest_framework import generics
from rest_framework import permissions
from manager.serializers.order.order import ManagerOrderSerializer
from manager.serializers.order_requests.request import OrderRequestCreateSerializer
from product.models.bag.order import Order

class ManagerOrderList(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = ManagerOrderSerializer
    permission_classes = (permissions.IsAuthenticated, )

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return OrderRequestCreateSerializer
        return super().get_serializer_class()


class ManagerOrderDetail(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'
    queryset = Order.objects.all()
    serializer_class = ManagerOrderSerializer
    permission_classes = (permissions.IsAuthenticated, )