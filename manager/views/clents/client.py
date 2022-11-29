from rest_framework import generics
from rest_framework import permissions
from manager.models.clients.client import Client
from manager.serializers.client.client import ClientSerializer


class ClientList(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = (permissions.IsAuthenticated, )


class ClientDetail(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = (permissions.IsAuthenticated, )