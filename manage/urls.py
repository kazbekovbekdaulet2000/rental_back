from django.urls import path
from manage.views.products import ManageProductDetail, ManageProductList
from manage.views.statistics import ManageStatisticsDetail

urlpatterns = [
    path("products/", ManageProductList.as_view()),
    path("products/<int:id>/", ManageProductDetail.as_view()),
    path("statistics/", ManageStatisticsDetail.as_view()),
]
