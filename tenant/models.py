from django.db import models
from common.custom_model import AbstractModel
from django_tenants.models import TenantMixin, DomainMixin


class TenantClient(AbstractModel, TenantMixin):
    name = models.CharField(max_length=255)
    paid_until = models.DateField()
    on_trial = models.BooleanField()
    trial_start = models.DateTimeField()
    trial_end = models.DateTimeField()

    # default true, schema will be automatically created and synced when it is saved
    auto_create_schema = True


class TenantDomain(DomainMixin):
    pass
