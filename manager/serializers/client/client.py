from manager.models.clients.client import Client
from rest_framework import serializers
from manager.serializers.history_abstract import LogEntryHistorySerializer


class ClientSerializer(serializers.ModelSerializer, LogEntryHistorySerializer):
    class Meta:
        model = Client
        fields = "__all__"
