from rest_framework import generics
from product.models.bag.order import Order
from product.serializers.order import OrderCreateSerializer


class CreateOrderView(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderCreateSerializer