from django.db import models
from common.custom_model import AbstractModel
from django.utils.translation import gettext_lazy as _


def file_dir(instance, filename):
    return f"grant/{filename}"


class GrantForm(AbstractModel):
    full_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    instagram_url = models.URLField()
    portfolio_url = models.URLField()
    description = models.TextField(max_length=5192)
    file = models.FileField(upload_to=file_dir, null=True)
    date = models.DateField()
    comment = models.TextField(max_length=5192, null=True)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.full_name} - {self.phone}"

    class Meta:
        ordering = ('-created_at', )
        verbose_name = 'Грант'
        verbose_name_plural = 'Гранты'
