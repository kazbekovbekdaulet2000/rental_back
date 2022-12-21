from rest_framework import serializers
from manager.models.inventory.inventory_tarif import InventoryTarif
from product.models.product import Product


class InventoryTarifProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'slug', 'name_kk', 'name_ru')


class InventoryTarifSerializer(serializers.ModelSerializer):
    class Meta:
        model = InventoryTarif
        fields = "__all__"
        read_only_fields = ('id', 'inventory')

    def validate(self, attrs):
        if('name' in attrs and 'price' in attrs):
            tarif = InventoryTarif.objects.filter(
                inventory_id=self.context['view'].kwargs['inventory_id'], 
                name=attrs['name'], 
                price=attrs['price'], 
                default=False
            )
            if(tarif.count() > 0):
                raise serializers.ValidationError({'': 'Тариф уже существует'})
        return super().validate(attrs)

    def create(self, validated_data):
        validated_data['inventory_id'] = self.context['view'].kwargs['inventory_id']
        return super().create(validated_data)
    
    def update(self, instance, validated_data):
        if 'default' in validated_data:
            prev_tarif = instance.inventory.default_tarif
            if(prev_tarif):
                prev_tarif.default = False
                prev_tarif.save()
        return super().update(instance, validated_data)


class InventoryTarifBulkCreateItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = InventoryTarif
        fields = ('id', 'name', 'default', 'price', 'product_set')


class InventoryTarifBulkCreateSerializer(serializers.Serializer):
    list = InventoryTarifBulkCreateItemSerializer(many=True, write_only=True)

    def create(self, validated_data):
        inventory_id = self.context['view'].kwargs['inventory_id']
        return InventoryTarif.objects.bulk_create([
            InventoryTarif(**obj, inventory_id=inventory_id) for obj in validated_data.get('list')
        ])
