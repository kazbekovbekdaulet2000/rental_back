from django.db import models
from common.custom_model import AbstractModel
from common.image_progressive import create_thumbnail, has_changed
from manager.models.inventory.inventory import Inventory
from auditlog.registry import auditlog
from auditlog.models import AuditlogHistoryField


class InventoryPhoto(AbstractModel):
    inventory = models.ForeignKey(Inventory, on_delete=models.CASCADE, related_name='photos')
    photo = models.ImageField(upload_to='inventory', null=False)
    history = AuditlogHistoryField()

    def save(self, *args, **kwargs):
        if (has_changed(self, 'photo') and self.type == 0):
            self.photo = create_thumbnail(self.photo, 720)
        super(InventoryPhoto, self).save(*args, **kwargs)
        
    class Meta:  
        ordering = ('-created_at', )

auditlog.register(InventoryPhoto)