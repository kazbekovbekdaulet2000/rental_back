from rest_framework import generics
from rest_framework import permissions
from product.models.bag.bag import UserBag
from product.models.bag.bag_product import UserBagItem
from product.serializers.bag import UserBagCreateSerializer, UserBagItemCreateSerializer, UserBagItemSerializer, UserBagSerializer


class CreateUserBag(generics.CreateAPIView):
    permission_classes = (permissions.AllowAny, )
    queryset = UserBag.objects.all()
    serializer_class = UserBagCreateSerializer


class UserBagList(generics.RetrieveAPIView):
    lookup_field = 'id'
    lookup_url_kwarg = 'uuid'
    permission_classes = (permissions.AllowAny, )
    queryset = UserBag.objects.all()
    serializer_class = UserBagSerializer


class UserBagProductsList(generics.ListCreateAPIView):
    permission_classes = (permissions.AllowAny, )
    pagination_class = None

    def get_queryset(self):
        return UserBagItem.objects.filter(order_id=self.kwargs['uuid'])

    def get_serializer_class(self):
        if (self.request.method == 'POST'):
            return UserBagItemCreateSerializer
        return UserBagItemSerializer


class UserBagDetail(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'
    lookup_url_kwarg = 'id'
    permission_classes = (permissions.AllowAny, )
    queryset = UserBagItem.objects.all()

    def get_serializer_class(self):
        if (self.request.method == "GET"):
            return UserBagItemSerializer
        return UserBagItemCreateSerializer