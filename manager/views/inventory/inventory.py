from rest_framework import generics
from rest_framework import permissions
from manager.models.inventory.inventory import Inventory
from manager.models.inventory.inventory_photo import InventoryPhoto
from manager.serializers.inventory.inventory import InventorySerializer
from manager.serializers.inventory.inventory_image import InventoryPhotoSerializer


class InventoryList(generics.ListCreateAPIView):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer
    permission_classes = (permissions.IsAuthenticated, )


class InvenoryDetail(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer
    permission_classes = (permissions.IsAuthenticated, )


class InvenoryImagesList(generics.ListCreateAPIView):
    lookup_field = 'inventory_id'
    serializer_class = InventoryPhotoSerializer
    permission_classes = (permissions.IsAuthenticated, )

    def get_queryset(self):
        return InventoryPhoto.objects.filter(inventory_id=self.kwargs[self.lookup_field])
