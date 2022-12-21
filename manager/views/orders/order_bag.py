from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework import permissions
from product.models.bag.order import Order
from product.serializers.bag import UserBagSerializer


class ManagerOrderBagDetail(generics.RetrieveUpdateAPIView):
    queryset = None
    serializer_class = UserBagSerializer
    permission_classes = (permissions.IsAuthenticated, )

    def get_object(self):
        filter_kwargs = {'id': self.kwargs['id']}
        obj = get_object_or_404(Order, **filter_kwargs)
        self.check_object_permissions(self.request, obj.bag)
        return obj.bag
