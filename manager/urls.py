from django.urls import path
from manager.models.inventory.inventory import Inventory
from manager.models.clients.client import Client
from manager.views.clents.client import ClientDetail, ClientList
from manager.views.clents.client_passport import ClientPassportIndividualList, ClientPassportLegalList
from manager.views.clents.ticks import ClientTicksDetail, ClientTicksList
from manager.views.inventory.inventory import InvenoryDetail, InvenoryImagesList, InventoryList
from manager.views.inventory.inventory_status import InventoryStatusList
from manager.views.log import LogEntryList
from manager.views.object_history import LogEntryObjectHistory
from manager.views.orders.order_bag import ManagerOrderBagDetail
from manager.views.orders.orders import ManagerOrderDetail, ManagerOrderList
from manager.views.product_statistic import ManagerStatisticProducts
from manager.views.rentinhand import ManagerRentInHandFile
from manager.views.statistic import ManagerStatistics


urlpatterns = [
    path("statistics/", ManagerStatistics.as_view()),
    path("statistics/products/", ManagerStatisticProducts.as_view()),
    path('rentinhand/upload/', ManagerRentInHandFile.as_view()),

    # # inventories
    # path('inventories/status/', InventoryStatusList.as_view()),
    # path('inventories/', InventoryList.as_view()),
    # path('inventories/<int:id>/', InvenoryDetail.as_view()),
    # path('inventories/<int:id>/history/', LogEntryObjectHistory.as_view(model=Inventory, lookup_field='id')),
    # path('inventories/<int:inventory_id>/images/', InvenoryImagesList.as_view()),

    # # clients
    # path('clients/', ClientList.as_view()),
    # path('clients/<int:id>/', ClientDetail.as_view()),
    # path('clients/<int:id>/history/', LogEntryObjectHistory.as_view(model=Client, lookup_field='id')),
    # path('clients/<int:id>/legal/passports/', ClientPassportLegalList.as_view()),
    # path('clients/<int:id>/individual/passports/', ClientPassportIndividualList.as_view()),

    # # clients ticks
    # path('clients/ticks/', ClientTicksList.as_view()),
    # path('clients/ticks/<int:id>/', ClientTicksDetail.as_view()),

    # # orders
    # path('orders/', ManagerOrderList.as_view()),
    # path('orders/<int:id>/', ManagerOrderDetail.as_view()),
    # path('orders/<int:id>/bag/', ManagerOrderBagDetail.as_view()),

    # # LogEntry
    # path('logs/', LogEntryList.as_view()),
]