from auditlog.models import LogEntry
from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework import permissions
from manager.serializers.log import LogEntrySerializer


class LogEntryHistory(generics.ListAPIView):
    model = None
    queryset = LogEntry.objects.all()
    serializer_class = LogEntrySerializer
    permission_classes = (permissions.IsAuthenticated, )

    def get_queryset(self):
        return LogEntry.objects.get_for_model(model=self.model)


class LogEntryObjectHistory(generics.ListAPIView):
    model = None
    lookup_field = None
    queryset = LogEntry.objects.all()
    serializer_class = LogEntrySerializer
    permission_classes = (permissions.IsAuthenticated, )

    def get_queryset(self):
        obj = get_object_or_404(self.model, id=self.kwargs[self.lookup_field])
        return LogEntry.objects.get_for_object(obj)
