from django.contrib import admin
from manager.models.clients.client import Client
from manager.models.clients.client_tick import ClientTick
from manager.models.clients.client_discount import ClientDiscount
from manager.models.clients.passport_individual import ClientPassportIndividual
from manager.models.clients.passport_legal import ClientPassportLegal
from manager.models.inventory.inventory import Inventory
from manager.models.inventory.inventory_photo import InventoryPhoto
from manager.models.inventory.inventory_status import InventoryStatus
from manager.models.inventory.inventory_tarif import InventoryTarif


admin.site.register([
    Client,
    ClientTick,
    ClientDiscount,
    ClientPassportIndividual,
    ClientPassportLegal
])
admin.site.register([
    Inventory,
    InventoryPhoto,
    InventoryStatus,
    InventoryTarif
])
