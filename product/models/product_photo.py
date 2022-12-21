from django.db import models
from common.custom_model import AbstractModel
from django.utils.translation import gettext_lazy as _
from common.image_progressive import create_thumbnail, has_changed
from product.models.product import Product
from product.models.service import Service


class ProductPhotoType(models.IntegerChoices):
    CAROUSEL = 0, _("Карусель")
    PREVIEW = 1, _("Превью")


def thumb_dir(instance, filename):
    if(instance.service):
        return f"products/{instance.service.slug}/{filename}"
    if(instance.product):
        return f"products/{instance.product.slug}/{filename}"
    return "products"


class ProductPhoto(AbstractModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="images", null=True, blank=True)
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name="images", null=True, blank=True)
    image = models.ImageField(verbose_name=_('Фото'), null=False, blank=True, upload_to=thumb_dir)
    image_thumb360 = models.ImageField(verbose_name=_('Фото (360px)'), upload_to=thumb_dir, max_length=500, null=True, blank=True)
    image_thumb720 = models.ImageField(verbose_name=_('Фото (720px)'), upload_to=thumb_dir, max_length=500, null=True, blank=True)
    image_thumb1080 = models.ImageField(verbose_name=_('Фото (1080px)'), upload_to=thumb_dir, max_length=500, null=True, blank=True)
    type = models.PositiveIntegerField(default=ProductPhotoType.CAROUSEL, choices=ProductPhotoType.choices)
    
    def __str__(self):
        if(self.service):
            return f"{self.service.name_ru}"
        if(self.product):
            return f"{self.product.name_ru}"
        return self.image

    def save(self, *args, **kwargs):
        if (has_changed(self, 'image') and self.type == 0):
            self.image_thumb1080 = create_thumbnail(self.image, 1080)
            self.image_thumb720 = create_thumbnail(self.image, 720)
            self.image_thumb360 = create_thumbnail(self.image, 360)
        super(ProductPhoto, self).save(*args, **kwargs)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Фото'
        verbose_name_plural = 'Фотографии'