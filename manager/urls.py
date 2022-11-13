from django.urls import path
from manager.views.product_statistic import ManagerStatisticProducts

from manager.views.rentinhand import ManagerRentInHandFile
from manager.views.statistic import ManagerStatistics

urlpatterns = [
    path("statistics/", ManagerStatistics.as_view()),
    path("statistics/products/", ManagerStatisticProducts.as_view()),
    path('rentinhand/upload/', ManagerRentInHandFile.as_view())
]
