from auditlog.models import LogEntry
from rest_framework import generics
from rest_framework import permissions
from manager.serializers.log import LogEntrySerializer


class LogEntryList(generics.ListAPIView):
    queryset = LogEntry.objects.all()
    serializer_class = LogEntrySerializer
    permission_classes = (permissions.IsAuthenticated, )
