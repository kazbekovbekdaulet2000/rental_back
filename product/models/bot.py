from django.db import models
from common.custom_model import AbstractModel

class BotUser(AbstractModel):
    user_id = models.PositiveBigIntegerField(unique=True, primary_key=True, max_length=255)
    name = models.CharField(max_length=255)
    approved = models.BooleanField(default=False, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Рассылка'
        verbose_name_plural = 'Рассылка'