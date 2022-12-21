from django.http import Http404
from django.shortcuts import get_object_or_404
from rest_framework import generics, mixins
from rest_framework import permissions
from manager.models.clients.passport_legal import ClientPassportLegal
from manager.models.clients.passport_individual import ClientPassportIndividual
from manager.serializers.client.client_passport import ClientPassportIndividualSerializer, ClientPassportLegalSerializer
from manager.views.clents.client import Client


class ClientPassportLegalList(generics.RetrieveUpdateDestroyAPIView, mixins.CreateModelMixin):
    queryset = ClientPassportLegal.objects.all()
    serializer_class = ClientPassportLegalSerializer
    permission_classes = (permissions.IsAuthenticated, )

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get_object(self):
        obj = get_object_or_404(Client, **{'id': self.kwargs['client_id']})
        if obj.legal_passport == None:
            raise Http404(
                "No %s matches the given query." % Client._meta.object_name
            )
        self.check_object_permissions(self.request, obj.legal_passport)
        return obj.legal_passport


class ClientPassportIndividualList(generics.RetrieveUpdateDestroyAPIView, mixins.CreateModelMixin):
    queryset = ClientPassportIndividual.objects.all()
    serializer_class = ClientPassportIndividualSerializer
    permission_classes = (permissions.IsAuthenticated, )

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get_object(self):
        obj = get_object_or_404(Client, **{'id': self.kwargs['client_id']})
        if obj.individual_passport == None:
            raise Http404(
                "No %s matches the given query." % Client._meta.object_name
            )
        self.check_object_permissions(self.request, obj.individual_passport)
        return obj.individual_passport