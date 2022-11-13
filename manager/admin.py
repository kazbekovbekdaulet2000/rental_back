from django.contrib import admin
from manager.models.rentinhand_inventory import ManagerRentInHandInventory
from manager.models.rentinhand_order import ManagerRentInHandOrder
from manager.models.statistics.product_statistic import ManagerProductStat
from manager.models.statistics.statistic import ManagerStat


admin.site.register([ManagerRentInHandOrder, ManagerRentInHandInventory, ManagerStat, ManagerProductStat])
