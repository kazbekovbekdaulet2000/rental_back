from django.db import models
from common.custom_model import AbstractModel
from django.contrib.postgres.fields import ArrayField
from ckeditor_uploader.fields import RichTextUploadingField
from pytils.translit import slugify
from django.utils.translation import gettext_lazy as _


class Service(AbstractModel):
    name_ru = models.CharField(max_length=255)
    name_kk = models.CharField(max_length=255)
    description_ru = RichTextUploadingField(null=True, blank=True)
    description_kk = RichTextUploadingField(null=True, blank=True)
    daily_price = models.IntegerField(null=False, blank=False)
    tags = ArrayField(base_field=models.CharField(max_length=255), null=True, blank=True)
    slug = models.SlugField(null=True, blank=True, unique=True)
    active = models.BooleanField(default=True, null=False)
    
    def __str__(self):
        return self.name_ru

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name_ru)
        return super().save(*args, **kwargs)

    def telegram_detail(self, order, days):
        return f"""<b>{order}. {self.name_ru}</b>\nСтоимость: {self.daily_price} KZT x {days} суток = <b>{self.daily_price * days} KZT</b>\n\n"""

    class Meta:
        ordering = ('created_at',)
        verbose_name = 'Сервис'
        verbose_name_plural = 'Сервисы'
        index_together = (('id', 'slug'), )
