from django.db import models
from common.custom_model import AbstractModel
from django.core.validators import MaxLengthValidator, MinLengthValidator
from auditlog.registry import auditlog
from auditlog.models import AuditlogHistoryField


class ClientPassportLegal(AbstractModel):
    bin = models.CharField(max_length=12, validators=(MinLengthValidator(12), MaxLengthValidator(12)))
    address = models.CharField(max_length=255)
    director = models.CharField(max_length=255)
    contacts = models.TextField(max_length=512)
    history = AuditlogHistoryField()
   
    class Meta:  
        ordering = ('-created_at', )

auditlog.register(ClientPassportLegal)