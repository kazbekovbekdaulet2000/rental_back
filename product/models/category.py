from django.db import models
from common.custom_model import AbstractModel
from django.contrib.postgres.fields import ArrayField

CATEGORY_TYPE = (
    ('equipment', 'Оборудование'),
    ('service', 'Сервис'),
)

class Category(AbstractModel):
    name_ru = models.CharField(max_length=255)
    name_kk = models.CharField(max_length=255)
    icon = models.FileField(upload_to='category_icon', null=True, blank=True)
    tags = ArrayField(base_field=models.CharField(max_length=255), null=True, blank=True)
    parent_category = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    slug = models.SlugField(null=True, blank=True, unique=True)
    type = models.CharField(max_length=255,choices=CATEGORY_TYPE, null=True, blank=True)

    def __str__(self):
        return self.name_ru

    def save(self, *args, **kwargs):
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'