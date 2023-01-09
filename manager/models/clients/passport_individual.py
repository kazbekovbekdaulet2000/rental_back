from django.db import models
from common.custom_model import AbstractModel
from django.core.validators import MaxLengthValidator, MinLengthValidator
from auditlog.registry import auditlog
from auditlog.models import AuditlogHistoryField


class ClientPassportIndividual(AbstractModel):
    iin = models.CharField(max_length=12, validators=(MinLengthValidator(12), MaxLengthValidator(12)))
    document_number = models.CharField(max_length=255)
    issue = models.CharField(max_length=255)
    issue_date = models.DateField()
    issue_date_end = models.DateField()
    birth_date = models.DateField(null=True)
    history = AuditlogHistoryField()

    class Meta:  
        ordering = ('-created_at', )

auditlog.register(ClientPassportIndividual)