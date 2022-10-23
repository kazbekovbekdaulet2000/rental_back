import math
from django.contrib import admin
from product.models.bag.bag import UserBag
from product.models.bag.bag_product import UserBagItem
from product.models.bag.order import Order
from product.models.bot import BotUser
from product.models.eav import Attribute, Value
from product.models.product import Product
from product.models.product_photo import ProductPhoto
from product.models.category import Category
from product.forms import ProductForm, CategoryForm
from product.models.product_service import ProductService
from product.models.product_set import ProductSet
from product.models.service import Service


class ProductPhotoAdmin(admin.TabularInline):
    fields = ('image', 'type')
    model = ProductPhoto
    extra = 0

class ProductSetAdmin(admin.TabularInline):
    fields = ('set_product',)
    fk_name = 'product'
    model = ProductSet
    extra = 0


class ServicePhotoAdmin(admin.TabularInline):
    fields = ('image', 'type')
    model = ProductPhoto
    extra = 0


class ProductSpecAdmin(admin.TabularInline):
    fields = ('attribute', 'value_ru', 'value_kk')
    model = Value
    extra = 0


class ProductServiceAdmin(admin.TabularInline):
    fields = ('service', 'required')
    model = ProductService
    extra = 0


class ProductAdmin(admin.ModelAdmin):
    list_display = ("name_ru", "daily_price",)
    prepopulated_fields = {"slug": ("name_ru",)}
    form = ProductForm
    inlines = (ProductPhotoAdmin, ProductSetAdmin, ProductSpecAdmin, ProductServiceAdmin)


class ServiceAdmin(admin.ModelAdmin):
    list_display = ("name_ru", "daily_price")
    prepopulated_fields = {"slug": ("name_ru",)}
    inlines = (ServicePhotoAdmin, )


class UserBagItemAdmin(admin.TabularInline):
    fields = ('product', 'count')
    readonly_fields = ('product', 'count')
    model = UserBagItem
    extra = 0

    def has_delete_permission(self, *args, **kwargs) -> bool:
        return False

    def has_add_permission(self, *args, **kwargs) -> bool:
        return False

    def has_change_permission(self, *args, **kwargs) -> bool:
        return False


class UserBagAdmin(admin.ModelAdmin):
    readonly_fields = ('previous_order', 'services_price',
                       'products_price', 'total_price', 'services__str')
    inlines = (UserBagItemAdmin, )


class OrderItemAdmin(admin.TabularInline):
    fields = ('product', 'count')
    model = UserBagItem
    extra = 0


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone', 'approved', 'start_time', 'end_time')
    readonly_fields = ('bag', 'total_time', 'total_price', 'services_price')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name_ru", "name_kk")
    form = CategoryForm


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(ProductPhoto)
admin.site.register(Attribute)
admin.site.register(BotUser)
admin.site.register(ProductSet)
admin.site.register(ProductService)
admin.site.register(UserBag, UserBagAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Service, ServiceAdmin)
