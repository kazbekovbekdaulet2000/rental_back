from django.urls import path
from manage.views.products import ManageProductDetail, ManageProductList
from manage.views.statistic_products import ManageStatisticProducts
from manage.views.statistics import ManageStatisticsDetail

urlpatterns = [
    path("products/", ManageProductList.as_view()),
    path("products/<int:id>/", ManageProductDetail.as_view()),
    path("statistics/", ManageStatisticsDetail.as_view()),
    path("statistics/products/", ManageStatisticProducts.as_view())
]
