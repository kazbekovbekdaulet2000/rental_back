from rest_framework import generics
from rest_framework import permissions
from manager.models.inventory.inventory import Inventory
from manager.models.inventory.inventory_photo import InventoryPhoto
from manager.serializers.inventory.inventory import InventorySerializer, InventoryCreateSerializer, InventoryUpdateSerializer, ManagerInventoryBulkCreateSerializer
from manager.serializers.inventory.inventory_image import InventoryPhotoBulkCreate, InventoryPhotoDetailSerializer, InventoryPhotoSerializer
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend


class InventoryList(generics.ListCreateAPIView):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer
    permission_classes = (permissions.IsAuthenticated, )
    filter_backends = (DjangoFilterBackend, SearchFilter)
    search_fields = ('name', 'unique_id')
    filterset_fields = ('category', 'status')

    def get_serializer_class(self):
        if self.request.method in permissions.SAFE_METHODS:
            return InventorySerializer
        return InventoryCreateSerializer


class ManagerInventoryBulkCreate(generics.CreateAPIView):
    serializer_class = ManagerInventoryBulkCreateSerializer
    permission_classes = (permissions.IsAuthenticated, )


class InvenoryDetail(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'
    queryset = Inventory.objects.all()
    serializer_class = InventoryCreateSerializer
    permission_classes = (permissions.IsAuthenticated, )

    def get_serializer_class(self):
        if self.request.method in permissions.SAFE_METHODS:
            return InventorySerializer
        if self.request.method == "POST":
            return InventoryCreateSerializer
        return InventoryUpdateSerializer


class InvenoryImagesList(generics.ListCreateAPIView):
    lookup_field = 'inventory_id'
    serializer_class = InventoryPhotoDetailSerializer
    permission_classes = (permissions.IsAuthenticated, )
    pagination_class = None

    def get_queryset(self):
        return InventoryPhoto.objects.filter(inventory_id=self.kwargs[self.lookup_field])


class InvenoryImageDelete(generics.DestroyAPIView):
    lookup_field = 'id'
    serializer_class = InventoryPhotoSerializer
    permission_classes = (permissions.IsAuthenticated, )

    def get_queryset(self):
        return InventoryPhoto.objects.filter(inventory_id=self.kwargs['inventory_id'])


class InvenoryImagesBulkCreate(generics.CreateAPIView):
    lookup_field = 'inventory_id'
    serializer_class = InventoryPhotoBulkCreate
    permission_classes = (permissions.IsAuthenticated, )
