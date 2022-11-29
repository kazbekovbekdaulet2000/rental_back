from manager.models.clients.passport_legal import ClientPassportLegal
from manager.models.clients.passport_individual import ClientPassportIndividual
from rest_framework import serializers


class ClientPassportLegalSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientPassportLegal
        fields = "__all__"


class ClientPassportIndividualSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientPassportIndividual
        fields = "__all__"
