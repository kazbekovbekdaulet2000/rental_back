from rest_framework import serializers
from manager.models.clients.client_tick import ClientTick
from manager.serializers.history_abstract import LogEntryHistorySerializer


class ClientTickSerializer(serializers.ModelSerializer, LogEntryHistorySerializer):
    class Meta:
        model = ClientTick
        fields = "__all__"
