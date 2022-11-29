from django.db import models
from common.custom_model import AbstractModel
from django.core.validators import RegexValidator
from auditlog.registry import auditlog
from auditlog.models import AuditlogHistoryField


class ClientTick(AbstractModel):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=9, validators=(RegexValidator("^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$"),), default='#000')
    comment = models.TextField(max_length=512, null=True)
    history = AuditlogHistoryField()


auditlog.register(ClientTick)