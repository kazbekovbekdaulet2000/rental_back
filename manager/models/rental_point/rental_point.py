from django.db import models
from common.custom_model import AbstractModel


class RentalPoint(AbstractModel):
    name = models.CharField(max_length=512, null=False)
    address = models.CharField(max_length=512, null=False)
    
    def __str__(self):
        return self.address