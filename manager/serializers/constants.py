from rest_framework import serializers
from manager.models.constants import ManagerContants


class ManagerContantsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ManagerContants
        fields = ['PRODUCT_TYPE', 'CATEGORIES', 'INVENTORY_CATEGORIES', 'CATEGORY_TYPE',
                  'CLIENT_ATTRACTION_METHOD', 'CLIENT_TYPE', 'CLIENT_TICKS',
                  'RENTAL_POINTS', 'APPLICATION_READY', 'PRODUCT_IMAGE_TYPE', 
                  'INVENTORY_TYPE', 'INVENTORY_STATUS', 'TARIF_TIME_PERIODS']