from rest_framework import serializers
from manager.models.inventory.inventory import Inventory
from manager.models.interchangeable.interchangeable import Interchangeable

class InterchangeableInventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = ('id', 'name', 'unique_id', 'status', 'category')


class InterchangeableSerializer(serializers.ModelSerializer):
    inventories = InterchangeableInventorySerializer(many=True, read_only=True)
    
    class Meta:
        model = Interchangeable
        fields = "__all__"