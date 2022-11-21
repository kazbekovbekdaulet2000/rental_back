from django.urls import path
from product.views.order import CreateOrderView
from product.views.product import ProductCategoryList, ProductList, ProductDetail
from product.views.category import CategoryList
from product.views.product import ProductRelatedList
from product.views.product_announcement import NewProductsList
from product.views.product_bag import CreateUserBag, UserBagList, UserBagDetail, UserBagProductsList


urlpatterns = [
  # categories
  path("categories/", CategoryList.as_view()),
  # products
  path("products/", ProductList.as_view()),
  path("products/all/", ProductCategoryList.as_view()),
  path('products/new/', NewProductsList.as_view()),
  path("products/<slug:slug>/", ProductDetail.as_view()),
  path("products/<slug:slug>/related/", ProductRelatedList.as_view()),

  # bag
  path("bag/", CreateUserBag.as_view()),
  path("bag/<uuid:uuid>/", UserBagList.as_view()), 
  path("bag/<uuid:uuid>/products/", UserBagProductsList.as_view()),
  path("bag/<uuid:uuid>/products/<int:id>/", UserBagDetail.as_view()),
  path("bag/<uuid:uuid>/order/", CreateOrderView.as_view()),
]
