import math
from django.db import models
from common.custom_model import AbstractModel
from django.contrib.postgres.fields import ArrayField
from ckeditor_uploader.fields import RichTextUploadingField
from manager.models.interchangeable.interchangeable import Interchangeable
from product.models.category import Category
from pytils.translit import slugify
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from auditlog.registry import auditlog
from auditlog.models import AuditlogHistoryField


PRODUCT_TYPE = (
    (0, 'Товар'),
    (2, 'Комплект')
)


class Product(AbstractModel):
    name_ru = models.CharField(max_length=255)
    name_kk = models.CharField(max_length=255)
    order = models.PositiveIntegerField(null=True, blank=True)
    articule = models.CharField(max_length=255, null=False, blank=False, unique=True)
    description_ru = RichTextUploadingField(null=True, blank=True)
    description_kk = RichTextUploadingField(null=True, blank=True)
    daily_price = models.IntegerField(null=False, blank=False)
    tags = ArrayField(base_field=models.CharField(max_length=255), null=True, blank=True)
    category = models.ForeignKey(Category, related_name="products", on_delete=models.CASCADE)
    slug = models.SlugField(null=True, blank=True, unique=True)

    instruction_video = models.URLField(verbose_name=_("Cсылка на инструкцию"), null=True, blank=True)
    amount = models.PositiveIntegerField(_("Количество продукции"), default=5)
    active = models.BooleanField(default=True, null=False)
    type = models.PositiveIntegerField(default=0, choices=PRODUCT_TYPE)
    
    related_products_array = ArrayField(base_field=models.PositiveIntegerField(), null=True, blank=True)
    parts = models.ManyToManyField(Interchangeable, related_name='products')

    history = AuditlogHistoryField()

    discount = None
    price = None
    tarif = None
    image = None

    def __str__(self):
        return self.name_ru

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        if(self.id):
            _discount = self.discounts.filter(
                discount__start_date__lte=timezone.now(),
                discount__end_date__gte=timezone.now()
            ).last()
            if(_discount):
                self.discount = _discount.discount_percent
                self.price = math.ceil(self.daily_price * _discount.discount_multiplier)
            else:
                self.price = self.daily_price

            images = self.images.filter(type=1)
            if images.count() > 0:
                self.image = images.first()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name_ru)
        return super().save(*args, **kwargs)

    class Meta:
        ordering = ('category', 'order','created_at',)
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        index_together = (('id', 'slug'), )


auditlog.register(Product)