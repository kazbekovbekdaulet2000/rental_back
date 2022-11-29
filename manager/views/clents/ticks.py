from rest_framework import generics
from rest_framework import permissions
from manager.models.clients.client_tick import ClientTick
from manager.serializers.client.client_tick import ClientTickSerializer


class ClientTicksList(generics.ListCreateAPIView):
    queryset = ClientTick.objects.all()
    serializer_class = ClientTickSerializer
    permission_classes = (permissions.IsAuthenticated, )


class ClientTicksDetail(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'
    queryset = ClientTick.objects.all()
    serializer_class = ClientTickSerializer
    permission_classes = (permissions.IsAuthenticated, )
