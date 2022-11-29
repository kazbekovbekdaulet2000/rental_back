from django.db import models
from common.custom_model import AbstractModel
from auditlog.registry import auditlog
from auditlog.models import AuditlogHistoryField


class InventoryStatus(AbstractModel):
    name = models.CharField(max_length=255)
    comment = models.TextField(max_length=512, null=True)
    disable = models.BooleanField(default=False)
    history = AuditlogHistoryField()


auditlog.register(InventoryStatus)