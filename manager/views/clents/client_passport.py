from rest_framework import generics
from rest_framework import permissions
from manager.models.clients.passport_legal import ClientPassportLegal
from manager.models.clients.passport_individual import ClientPassportIndividual
from manager.serializers.client.client_passport import ClientPassportLegalSerializer


class ClientPassportLegalList(generics.ListCreateAPIView):
    queryset = ClientPassportLegal.objects.all()
    serializer_class = ClientPassportLegalSerializer
    permission_classes = (permissions.IsAuthenticated, )
    pagination_class = None

    def get_queryset(self):
        return ClientPassportLegal.objects.filter(client_id=self.kwargs['id'])


class ClientPassportIndividualList(generics.ListCreateAPIView):
    queryset = ClientPassportIndividual.objects.all()
    serializer_class = ClientPassportLegalSerializer
    permission_classes = (permissions.IsAuthenticated, )
    pagination_class = None

    def get_queryset(self):
        return ClientPassportIndividual.objects.filter(client_id=self.kwargs['id'])
