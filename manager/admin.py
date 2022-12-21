from django.contrib import admin
from manager.models.clients.client import Client
from manager.models.clients.client_tick import ClientTick
from manager.models.clients.client_discount import ClientDiscount
from manager.models.clients.passport_individual import ClientPassportIndividual
from manager.models.clients.passport_legal import ClientPassportLegal
from manager.models.inventory.inventory import Inventory
from manager.models.inventory.inventory_category import InventoryCategory
from manager.models.inventory.inventory_photo import InventoryPhoto
from manager.models.inventory.inventory_schedule import InventorySchedule
from manager.models.inventory.inventory_status import InventoryStatus
from manager.models.inventory.inventory_tarif import InventoryTarif
from manager.models.interchangeable.interchangeable import Interchangeable
from manager.models.order.order import ManagerOrder
from manager.models.order.order_inventory import ManagerOrderInventory
from manager.models.rental_point.rental_point import RentalPoint


class InventoryTarifAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "inventory", "default")
    list_filter = ("price", )

admin.site.register(InventoryTarif, InventoryTarifAdmin)


class InventoryAdmin(admin.ModelAdmin):
    list_display = ("id", "buy_price")

admin.site.register(Inventory, InventoryAdmin)

admin.site.register([
    Client,
    ClientTick,
    ClientDiscount,
    ClientPassportIndividual,
    ClientPassportLegal
])

admin.site.register([
    Interchangeable,
    InventorySchedule,
    InventoryPhoto,
    InventoryStatus,
    InventoryCategory
])

admin.site.register([
    ManagerOrder,
    ManagerOrderInventory,
])

admin.site.register([RentalPoint, ])
