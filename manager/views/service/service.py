from rest_framework import generics
from rest_framework import permissions
from manager.serializers.service.service import (
    ManagerServiceSerializer,
    ManagerServiceDetailSerializer
)
from product.models.service import Service


class ManagerServiceList(generics.ListCreateAPIView):
    queryset = Service.objects.all()
    serializer_class = ManagerServiceSerializer
    permission_classes = (permissions.IsAuthenticated, )

    def get_serializer_class(self):
        return super().get_serializer_class()


class ManagerServiceDetail(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = "id"
    queryset = Service.objects.all()
    serializer_class = ManagerServiceDetailSerializer
    permission_classes = (permissions.IsAuthenticated, )

    def get_serializer_class(self):
        if self.request.method in permissions.SAFE_METHODS:
            return super().get_serializer_class()
        return ManagerServiceSerializer