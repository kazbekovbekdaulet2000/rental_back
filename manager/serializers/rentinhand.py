import json
from rest_framework import serializers
from dateutil import parser
from manager.models.rentinhand_inventory import ManagerRentInHandInventory
from manager.models.rentinhand_order import ManagerRentInHandOrder


class ManagerRentInHandSerializer(serializers.ModelSerializer):
    class Meta:
        model = ManagerRentInHandOrder
        fields = ('file', )

    def create(self, validated_data):
        f = validated_data.get('file')
        data = json.load(f)
        orders = data['array']

        for order in orders:
            inventories = []
            
            for inventory in order['inventories']:
                title = str(inventory['inventory']['title'])
                if(not inventory['kit_id']):
                    obj, _ = ManagerRentInHandInventory.objects.get_or_create(title=title, defaults={
                        'rnh_id': inventory['inventory']['rent_number'],
                        'amount_rent_sum': str(inventory['inventory']['amount_rent_sum']),
                        'price': inventory['sum']
                    })
                    inventories.append(obj.id)

            unique_id = order['id']
            obj, _ = ManagerRentInHandOrder.objects.get_or_create(order_id=unique_id, defaults={
                'sum_rental': order['sum_rental'],
                'created_at': parser.isoparse(order['created_at']),
                'start_time': parser.isoparse(order['time_start']),
                'end_time': parser.isoparse(order['time_end']),
                'file': None,
                'file_data': order,
                'inventories': inventories
            })
        return validated_data
