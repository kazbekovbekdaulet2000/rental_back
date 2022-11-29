from rest_framework import generics
from rest_framework import permissions
from manager.serializers.order.order import ManagerOrderSerializer
from product.models.bag.order import Order

class ManagerOrderList(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = ManagerOrderSerializer
    permission_classes = (permissions.IsAuthenticated, )


class ManagerOrderDetail(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'
    queryset = Order.objects.all()
    serializer_class = ManagerOrderSerializer
    permission_classes = (permissions.IsAuthenticated, )