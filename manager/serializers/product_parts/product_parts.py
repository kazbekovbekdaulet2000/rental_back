from rest_framework import serializers
from manager.models.inventory.inventory import Inventory
from manager.models.interchangeable.interchangeable import Interchangeable

class ManagerProductPartInventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = ('id', 'name', 'unique_id', 'status', 'category')


class ManagerProductPartSerializer(serializers.ModelSerializer):
    inventories = ManagerProductPartInventorySerializer(many=True, read_only=True)
    
    class Meta:
        model = Interchangeable
        fields = "__all__"