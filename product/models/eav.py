from tabnanny import verbose
from django.db import models
from product.models.product import Product

class Attribute(models.Model):
    attribute_ru = models.CharField(max_length=255, null=False, default='attribute_ru')
    attribute_kk = models.CharField(max_length=255, null=False, default='attribute_kk')

    def __str__(self):
        return self.attribute_ru

    class Meta:
        verbose_name = 'Аттрибут'
        verbose_name_plural = 'Аттрибуты'

class Value(models.Model):
    value_ru = models.CharField(max_length=255, null=False, default='value_ru')
    value_kk = models.CharField(max_length=255, null=False, default='value_kk')
    attribute = models.ForeignKey(Attribute, on_delete=models.CASCADE, null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='eav')

    def __str__(self):
        return self.value_ru

    class Meta:
        unique_together = ('attribute', 'product')
