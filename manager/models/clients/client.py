from django.db import models
from common.custom_model import AbstractModel
from common.image_progressive import create_thumbnail, has_changed
from manager.models.clients.client_tick import ClientTick
from django.contrib.auth import get_user_model
from auditlog.registry import auditlog
from auditlog.models import AuditlogHistoryField
import uuid 
from django.utils.translation import gettext_lazy as _

from manager.models.clients.passport_individual import ClientPassportIndividual
from manager.models.clients.passport_legal import ClientPassportLegal


User = get_user_model()


CLIENT_TYPE = (
    (0, 'Физическое лицо'),
    (1, 'Юридическое лицо'),
)

ATTRACTION_METHOD = (
    ('instagram', 'instagram'),
    ('telegram', 'telegram'),
    ('facebook', 'facebook'),
    ('google', 'google'),
    ('other', 'other')
)

class Client(AbstractModel):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=512, null=False)
    type = models.PositiveIntegerField(choices=CLIENT_TYPE, default=0)
    birth_date = models.DateField(null=False)
    attraction_method = models.CharField(max_length=255, choices=ATTRACTION_METHOD)
    comment = models.TextField(max_length=512, null=True)
    avatar = models.ImageField(null=True)
    tick = models.ManyToManyField(ClientTick)
    email = models.EmailField(null=True)
    phone = models.CharField(max_length=32)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    legal_passport = models.ForeignKey(ClientPassportLegal, on_delete=models.SET_NULL, null=True)
    individual_passport = models.ForeignKey(ClientPassportIndividual, on_delete=models.SET_NULL, null=True)

    history = AuditlogHistoryField()

    def save(self, *args, **kwargs):
        if (has_changed(self, 'avatar') and self.avatar):
            self.avatar = create_thumbnail(self.avatar, 640)
        super(Client, self).save(*args, **kwargs)


auditlog.register(Client)
