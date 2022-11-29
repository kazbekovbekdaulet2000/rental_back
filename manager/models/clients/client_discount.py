from django.db import models
from common.custom_model import AbstractModel
from manager.models.clients.client import Client
from django.core.validators import MaxValueValidator
from auditlog.registry import auditlog
from auditlog.models import AuditlogHistoryField


class ClientDiscount(AbstractModel):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='discounts')
    discount_percent = models.PositiveIntegerField(null=True, validators=(MaxValueValidator(99),))
    discount_amount = models.PositiveIntegerField(null=True)
    start_time = models.DateTimeField(null=True)
    end_time = models.DateTimeField(null=True)
    history = AuditlogHistoryField()


auditlog.register(ClientDiscount)