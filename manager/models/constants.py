from django.db import models
from manager.constants import InventoryStatusType
from manager.models.clients.client import ATTRACTION_METHOD, CLIENT_TYPE
from manager.models.clients.client_tick import ClientTick
from manager.models.inventory.inventory_category import InventoryCategory
from manager.models.inventory.inventory_status import InventoryStatus
from manager.models.inventory.inventory_tarif_time_period import InventoryTarifTimePeriod
from manager.models.rental_point.rental_point import RentalPoint
from product.models.category import CATEGORY_TYPE, Category
from product.models.product import PRODUCT_TYPE


def getTypeObject(TYPE: tuple[tuple]) -> list:
    return list(map(lambda res: {'id': res[0], 'label': res[1]}, TYPE))


class ManagerContants(models.Model):
    PRODUCT_TYPE = []
    PRODUCT_IMAGE_TYPE = []
    CATEGORIES = []
    INVENTORY_CATEGORIES = []
    CATEGORY_TYPE = []
    CLIENT_TYPE = []
    CLIENT_ATTRACTION_METHOD = []
    CLIENT_TICKS = []
    RENTAL_POINTS = []
    APPLICATION_READY = False
    INVENTORY_TYPE = None
    INVENTORY_STATUS = None
    TARIF_TIME_PERIODS = []

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.PRODUCT_TYPE = getTypeObject(PRODUCT_TYPE)
        self.PRODUCT_IMAGE_TYPE = getTypeObject(())
        self.CATEGORY_TYPE = getTypeObject(CATEGORY_TYPE)
        self.CLIENT_TYPE = getTypeObject(CLIENT_TYPE)
        self.CLIENT_ATTRACTION_METHOD = getTypeObject(ATTRACTION_METHOD)
        self.CLIENT_TICKS = map(lambda obj: {
            'id': obj.id,
            'name': obj.name,
            'code': obj.code,
            'comment': obj.comment
        }, ClientTick.objects.all())
        self.CATEGORIES = map(lambda obj: {
            'id': obj.id,
            'name_kk': obj.name_kk,
            'name_ru': obj.name_ru,
            'icon': obj.icon,
            'slug': obj.slug
        }, Category.objects.all())
        self.INVENTORY_CATEGORIES = map(lambda obj: {
            'id': obj.id,
            'name': obj.name,
            'comment': obj.comment,
            'prefix': obj.prefix
        }, InventoryCategory.objects.all())
        self.RENTAL_POINTS = map(lambda obj: {
            'id': obj.id,
            'name': obj.name,
            'address': obj.address
        }, RentalPoint.objects.all())
        self.INVENTORY_TYPE = map(lambda obj: {
            'id': obj.id,
            'name': obj.name,
            'comment': obj.comment,
            'status': obj.status
        }, InventoryStatus.objects.all())
        self.TARIF_TIME_PERIODS = map(lambda obj: {
            'id': obj.id,
            'time': obj.time,
        }, InventoryTarifTimePeriod.objects.all())
        self.INVENTORY_STATUS = getTypeObject(InventoryStatusType.choices)

    class Meta:
        managed = False
