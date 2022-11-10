import json
from rest_framework import serializers
from manage.models.rentinhand_inventory import RentInHandInventory
from manage.models.rentinhand_order import RentInHandOrder
from dateutil import parser


class RentInHandSerializer(serializers.ModelSerializer):
    class Meta:
        model = RentInHandOrder
        fields = ('file', )

    def create(self, validated_data):
        f = validated_data.get('file')
        data = json.load(f)
        orders = data['array']

        for order in orders:
            inventories = []
            for inventory in order['inventories']:
                title = str(inventory['inventory']['title'])
                obj, _ = RentInHandInventory.objects.get_or_create(title=title, defaults={
                    'amount_rent_sum': str(inventory['inventory']['amount_rent_sum']),
                    'price': inventory['sum']
                })
                inventories.append(obj.id)
            unique_id = order['id']
            obj, _ = RentInHandOrder.objects.get_or_create(order_id=unique_id, defaults={
                'sum_rental': order['sum_rental'],
                'start_time': parser.isoparse(order['time_start']),
                'end_time': parser.isoparse(order['time_end']),
                'file': None,
                'file_data': order,
                'inventories': inventories
            })
        return validated_data
