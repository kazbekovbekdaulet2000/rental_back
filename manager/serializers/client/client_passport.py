from manager.models.clients.client import Client
from manager.models.clients.passport_legal import ClientPassportLegal
from manager.models.clients.passport_individual import ClientPassportIndividual
from rest_framework import serializers


class ClientPassportLegalSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientPassportLegal
        fields = "__all__"
    
    def create(self, validated_data):
        legal_passport = super().create(validated_data)
        client = Client.objects.get(id=int(self.context['view'].kwargs['client_id']))
        client.legal_passport = legal_passport
        client.save()
        return legal_passport


class ClientPassportIndividualSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientPassportIndividual
        fields = "__all__"

    def create(self, validated_data):
        individual_passport = super().create(validated_data)
        client = Client.objects.get(id=int(self.context['view'].kwargs['client_id']))
        client.individual_passport = individual_passport
        client.save()
        return individual_passport