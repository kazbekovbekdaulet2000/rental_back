from manager.models.clients.client import Client
from rest_framework import serializers


class BaseClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = [ 'id', 'name', 'type', 'avatar', 'phone', 'email', 'user', 'tick', 'uuid' ]


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = "__all__"