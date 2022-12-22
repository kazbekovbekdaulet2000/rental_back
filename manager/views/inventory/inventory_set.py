from rest_framework import generics
from rest_framework import permissions
from manager.models.inventory.inventory_set import InventorySet, InventorySetItem
from manager.serializers.inventory.inventory_set import InventorySetItemCreateSerializer, InventorySetItemSerializer, InventorySetSerializer


class InventorySetList(generics.ListCreateAPIView):
    queryset = InventorySet.objects.all()
    serializer_class = InventorySetSerializer
    permission_classes = (permissions.IsAuthenticated, )


class InventorySetDetail(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'
    queryset = InventorySet.objects.all()
    serializer_class = InventorySetSerializer
    permission_classes = (permissions.IsAuthenticated, )


class InventorySetItemList(generics.ListCreateAPIView):
    queryset = InventorySetItem.objects.all()
    serializer_class = InventorySetItemSerializer
    permission_classes = (permissions.IsAuthenticated, )
    pagination_class = None

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return InventorySetItemCreateSerializer
        return super().get_serializer_class()

    def get_queryset(self):
        return InventorySetItem.objects.filter(set_id=self.kwargs['set_id'])


class InventorySetItemDetail(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'
    queryset = InventorySetItem.objects.all()
    serializer_class = InventorySetItemSerializer
    permission_classes = (permissions.IsAuthenticated, )

    def get_queryset(self):
        return InventorySetItem.objects.filter(set_id=self.kwargs['set_id'])
