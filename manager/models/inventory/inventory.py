from django.db import models
from common.custom_model import AbstractModel
from manager.models.inventory.inventory_category import InventoryCategory
from manager.models.inventory.inventory_status import InventoryStatus
from manager.constants import InventoryTarifType
from auditlog.registry import auditlog
from auditlog.models import AuditlogHistoryField
from manager.models.rental_point.rental_point import RentalPoint


class Inventory(AbstractModel):
    name = models.CharField(max_length=255, null=False)
    unique_id = models.CharField(max_length=32, unique=True)
    status = models.ForeignKey(InventoryStatus, on_delete=models.DO_NOTHING)
    buy_price = models.PositiveIntegerField(null=True)
    buy_date = models.DateField(null=True)
    comment = models.TextField(max_length=1024, null=True)
    category = models.ForeignKey(InventoryCategory, on_delete=models.CASCADE)
    
    #rental_statuses 
    rent_point = models.ForeignKey(RentalPoint, on_delete=models.DO_NOTHING)
    rent_count = models.PositiveIntegerField(default=0)
    rent_money_amount = models.FloatField(default=0)

    # non db fields
    history = AuditlogHistoryField()
    default_tarif = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if(self.id):
            tarifs = self.tarifs.filter(default=True)
            self.default_tarif = tarifs.first() if tarifs.count() > 0 else None
    
    def is_free(self, start_at, end_at):
        # ********_______________************* <- schedule from db
        # ___*************____________________ <- request to check = FALSE
        # _____________****************_______ <- request to check = FALSE
        # ________**********__________________ <- request to check = TRUE
        # ___________**********_______________ <- request to check = TRUE
        schedules = self.schedule.filter(completed=False)
        
        schedule_start = schedules.filter(start_at__lt=start_at, end_at__gt=start_at)
        if(schedule_start.count() > 0): 
            return False
        
        schedule_end = schedules.filter(start_at__lt=end_at, end_at__gt=end_at)
        if(schedule_end.count() > 0): 
            return False
        
        return True

    def __str__(self):
        return f"{self.name} ({self.unique_id})"
        
    class Meta:  
        ordering = ('-created_at', )


auditlog.register(Inventory)