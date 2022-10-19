from django.db import models
from common.custom_model import AbstractModel
from django.contrib.postgres.fields import ArrayField
from ckeditor_uploader.fields import RichTextUploadingField
from product.models.category import Category
from pytils.translit import slugify
from django.utils.translation import gettext_lazy as _


PRODUCT_TYPE = (
    (0, 'товар'),
    (1, 'сет товаров')
)

class Product(AbstractModel):
    name_ru = models.CharField(max_length=255)
    name_kk = models.CharField(max_length=255)
    articule = models.CharField(max_length=255, null=False, blank=False, unique=True)
    description_ru = RichTextUploadingField(null=True, blank=True)
    description_kk = RichTextUploadingField(null=True, blank=True)
    daily_price = models.IntegerField(null=False, blank=False)
    tags = ArrayField(base_field=models.CharField(max_length=255), null=True, blank=True)
    category = models.ForeignKey(Category, related_name="products", on_delete=models.CASCADE)
    slug = models.SlugField(null=True, blank=True, unique=True)
    parent_product = models.ForeignKey('self', on_delete=models.SET_NULL, related_name="child_products", blank=True, null=True)
    active = models.BooleanField(default=True, null=False)
    type = models.PositiveIntegerField(default=0, choices=PRODUCT_TYPE)
    set_products = models.ManyToManyField('self', related_name="set_products", blank=True, null=True)
    related_products = models.ManyToManyField('self', related_name="related_products", blank=True, null=True)
    instruction_video = models.URLField(verbose_name=_("Cсылка на инструкцию"), null=True, blank=True)
    amount = models.PositiveIntegerField(_("Количество продукции"), default=5)

    def __str__(self):
        return self.name_ru

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name_ru)
        return super().save(*args, **kwargs)

    class Meta:
        ordering = ('created_at',)
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        index_together = (('id', 'slug'), )
