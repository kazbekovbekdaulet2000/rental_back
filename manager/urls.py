from django.urls import path
from manager.models.inventory.inventory import Inventory
from manager.models.clients.client import Client
from manager.views.clents.client import ClientDetail, ClientList
from manager.views.clents.client_passport import ClientPassportIndividualList, ClientPassportLegalList
from manager.views.clents.ticks import ClientTicksDetail, ClientTicksList
from manager.views.constants import ConstantsView
from manager.views.interchangeables.interchangeables import ManagerInterchangeableDetail, ManagerInterchangeableList
from manager.views.inventory.inventory import InvenoryDetail, InvenoryImageDelete, InvenoryImagesBulkCreate, InvenoryImagesList, InventoryList, ManagerInventoryBulkCreate
from manager.views.inventory.inventory_set import InventorySetDetail, InventorySetItemDetail, InventorySetItemList, InventorySetList
from manager.views.inventory.inventory_status import InventoryStatusList
from manager.views.inventory.inventory_tarif import InventoryTarifBulkCreate, InventoryTarifDetail, InventoryTarifList, InventoryTarifProducts
from manager.views.object_history import LogEntryObjectHistory
from manager.views.order_requests.requests import OrderRequestDetail, OrderRequestList
from manager.views.product.product import ManagerProductDetail, ManagerProductRelatedList, ManagerProductsList
from manager.views.product.product_image import ManagerProductImageBulkCreate, ManagerProductImageDelete, ManagerProductImageList
from manager.views.product.product_set import ManagerProductSetBulkCreate, ManagerProductSetDetail, ManagerProductSetList
from manager.views.interchangeables.product_parts import ManagerProductInterchangeableList, ManagerProductInterchangeableDetail
from manager.views.service.service import ManagerServiceDetail, ManagerServiceList
from manager.views.service.service_images import ManagerServiceImageDelete, ManagerServiceImageList
from product.models.product import Product


urlpatterns = [
    # constants
    path("constants/", ConstantsView.as_view()),

    # products
    path('products/', ManagerProductsList.as_view()),
    path('products/<int:id>/', ManagerProductDetail.as_view()),
    path('products/<int:id>/set/', ManagerProductSetList.as_view()),
    path('products/<int:id>/set/bulk_create/', ManagerProductSetBulkCreate.as_view()),
    path('products/<int:product_id>/set/<int:id>/', ManagerProductSetDetail.as_view()),
    path('products/<int:product_id>/images/', ManagerProductImageList.as_view()),
    path('products/<int:product_id>/images/<int:id>/', ManagerProductImageDelete.as_view()),
    path('products/<int:product_id>/images/bulk_create/', ManagerProductImageBulkCreate.as_view()),
    path('products/<int:product_id>/related_product/', ManagerProductRelatedList.as_view()),
    path('products/<int:id>/history/', LogEntryObjectHistory.as_view(model=Product, lookup_field='id')),

    # product interchangeables
    path('products/<int:product_id>/parts/', ManagerProductInterchangeableList.as_view()),
    path('products/<int:product_id>/parts/<int:id>/', ManagerProductInterchangeableDetail.as_view()), 

    # inventories
    path('inventories/status/', InventoryStatusList.as_view()),
    path('inventories/', InventoryList.as_view()),
    path('inventories/bulk_create/', ManagerInventoryBulkCreate.as_view()),
    path('inventories/<int:id>/', InvenoryDetail.as_view()),
    path('inventories/<int:id>/history/', LogEntryObjectHistory.as_view(model=Inventory, lookup_field='id')),
    path('inventories/<int:inventory_id>/images/', InvenoryImagesList.as_view()),
    path('inventories/<int:inventory_id>/images/<int:id>/', InvenoryImageDelete.as_view()),
    path('inventories/<int:inventory_id>/images/bulk_create/', InvenoryImagesBulkCreate.as_view()),
    path('inventories/<int:inventory_id>/tarifs/', InventoryTarifList.as_view()),
    path('inventories/<int:inventory_id>/tarifs/bulk_create/', InventoryTarifBulkCreate.as_view()),
    path('inventories/<int:inventory_id>/tarifs/<int:id>/', InventoryTarifDetail.as_view()),
    path('inventories/<int:inventory_id>/tarifs_products/', InventoryTarifProducts.as_view()),

    # interchangeables
    path('inventories/interchangeables/', ManagerInterchangeableList.as_view()),
    path('inventories/interchangeables/<int:id>/', ManagerInterchangeableDetail.as_view()),

    # inventory sets
    path('inventories/sets/', InventorySetList.as_view()),
    path('inventories/sets/<int:id>/', InventorySetDetail.as_view()),
    path('inventories/sets/<int:set_id>/items/', InventorySetItemList.as_view()),
    path('inventories/sets/<int:set_id>/items/<int:id>/', InventorySetItemDetail.as_view()),
    
    # services
    path('services/', ManagerServiceList.as_view()),
    path('services/<int:id>/', ManagerServiceDetail.as_view()),
    path('services/<int:id>/images/', ManagerServiceImageList.as_view()),
    path('services/<int:service_id>/images/<int:id>/', ManagerServiceImageDelete.as_view()),

    # clients
    path('clients/', ClientList.as_view()),
    path('clients/<int:id>/', ClientDetail.as_view()),
    path('clients/<int:id>/history/', LogEntryObjectHistory.as_view(model=Client, lookup_field='id')),
    path('clients/<int:client_id>/passport/legal/', ClientPassportLegalList.as_view()),
    path('clients/<int:client_id>/passport/individual/', ClientPassportIndividualList.as_view()),
    path('clients/ticks/', ClientTicksList.as_view()),
    path('clients/ticks/<int:id>/', ClientTicksDetail.as_view()),
    
    # # orders
    # path('orders/', ManagerOrderList.as_view()),
    # path('orders/<int:id>/', ManagerOrderDetail.as_view()),
    # path('orders/<int:id>/bag/', ManagerOrderBagDetail.as_view()),

    # manager orders
    path('requests/', OrderRequestList.as_view()),
    path('requests/<int:id>/', OrderRequestDetail.as_view()),
    # path('requests/<int:id>/inventories/', None),
    # path('requests/<int:id>/services/', None),
    # path('requests/<int:request_id>/inventories/<int:inventory_id>/to_rent/', None),
    # path('requests/<int:request_id>/inventories/<int:inventory_id>/submit_rent/', None),
    # path('requests/<int:request_id>/inventories/<int:inventory_id>/broken/', None),
]
