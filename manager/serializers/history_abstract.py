from rest_framework import serializers
from auditlog.models import LogEntry
from manager.serializers.log import LogEntrySerializer


class LogEntryHistorySerializer(serializers.Serializer):
    history = serializers.SerializerMethodField()

    def get_history(self, obj):
        return LogEntrySerializer(LogEntry.objects.get_for_object(obj), context={"request": self.context['request']}, many=True).data
