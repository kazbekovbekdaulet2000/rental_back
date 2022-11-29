from django.db import models
from common.custom_model import AbstractModel
from django.core.validators import MaxLengthValidator, MinLengthValidator
from manager.models.clients.client import Client
from auditlog.registry import auditlog
from auditlog.models import AuditlogHistoryField


class ClientPassportIndividual(AbstractModel):
    client = models.OneToOneField(Client, on_delete=models.CASCADE, related_name='individual_passports', null=True)
    iin = models.CharField(max_length=12, validators=(MinLengthValidator(12), MaxLengthValidator(12)))
    document_number = models.CharField(max_length=255)
    issue = models.CharField(max_length=255)
    issue_date = models.DateField()
    issue_date_end = models.DateField()
    history = AuditlogHistoryField()


auditlog.register(ClientPassportIndividual)