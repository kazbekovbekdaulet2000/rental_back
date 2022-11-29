from rest_framework import generics
from rest_framework import permissions
from manager.models.inventory.inventory_status import InventoryStatus
from manager.serializers.inventory.inventory_status import InventoryStatusSerializer


class InventoryStatusList(generics.ListCreateAPIView):
    queryset = InventoryStatus.objects.all()
    serializer_class = InventoryStatusSerializer
    permission_classes = (permissions.IsAuthenticated, )
    pagination_class = None
