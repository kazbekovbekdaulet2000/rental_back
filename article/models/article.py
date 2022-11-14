from django.db import models
from common.custom_model import AbstractModel
from django.contrib.postgres.fields import ArrayField
from ckeditor_uploader.fields import RichTextUploadingField
from pytils.translit import slugify
from django.utils.translation import gettext_lazy as _

from common.image_progressive import create_thumbnail, has_changed

def image_dir(instance, filename):
    return f"article/{instance.slug}/{filename}"

class Article(AbstractModel):
    title_ru = models.CharField(max_length=5196)
    title_kk = models.CharField(max_length=5196)
    order = models.PositiveIntegerField(null=True, blank=True)
    
    body_ru = RichTextUploadingField(null=True, blank=True)
    body_kk = RichTextUploadingField(null=True, blank=True)
    
    tags = ArrayField(base_field=models.CharField(max_length=255), null=True, blank=True)
    slug = models.SlugField(null=True, blank=True, unique=True)
    image = models.ImageField(verbose_name=_('Фото'), null=False, blank=True, upload_to=image_dir)

    active = models.BooleanField(default=True, null=False)
    products = ArrayField(base_field=models.PositiveIntegerField(), null=True, blank=True)

    def __str__(self):
        return self.title_ru

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title_ru)
        if (has_changed(self, 'image')):
            self.image = create_thumbnail(self.image, 1080)
        return super().save(*args, **kwargs)

    class Meta:
        ordering = ('created_at',)
        verbose_name = 'Обявление'
        verbose_name_plural = 'Обявления'
        index_together = (('id', 'slug'), )
