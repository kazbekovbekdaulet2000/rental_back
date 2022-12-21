from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework import permissions
from manager.models.inventory.inventory import Inventory
from manager.models.inventory.inventory_tarif import InventoryTarif
from manager.serializers.inventory.inventory_tarif import InventoryTarifBulkCreateSerializer, InventoryTarifProductSerializer, InventoryTarifSerializer
from product.models.product import Product


class InventoryTarifList(generics.ListCreateAPIView):
    serializer_class = InventoryTarifSerializer
    permission_classes = (permissions.IsAuthenticated, )

    def get_queryset(self):
        return InventoryTarif.objects.filter(inventory_id=self.kwargs['inventory_id']).order_by('-default')


class InventoryTarifProducts(generics.ListAPIView):
    serializer_class = InventoryTarifProductSerializer
    permission_classes = (permissions.IsAuthenticated, )
    pagination_class = None
    
    def get_object(self):
        obj = get_object_or_404(Inventory, id=self.kwargs['inventory_id'])
        self.check_object_permissions(self.request, obj)
        return obj

    def get_queryset(self):
        inventory = self.get_object()
        product_ids = inventory.product_parts.values_list('products', flat=True)
        return Product.objects.filter(id__in = product_ids)



class InventoryTarifBulkCreate(generics.CreateAPIView):
    serializer_class = InventoryTarifBulkCreateSerializer
    permission_classes = (permissions.IsAuthenticated, )


class InventoryTarifDetail(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'
    serializer_class = InventoryTarifSerializer
    permission_classes = (permissions.IsAuthenticated, )

    def get_queryset(self):
        return InventoryTarif.objects.filter(inventory_id=self.kwargs['inventory_id'])