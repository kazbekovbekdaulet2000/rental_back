from django.contrib import admin
from product.models.bag.bag import UserBag
from product.models.bag.bag_product import UserBagItem
from product.models.bag.order import Order
from product.models.bot import BotUser
from product.models.eav import Attribute, Value
from product.models.product import Product
from product.models.product_announcement import ProductAnnouncement
from product.models.product_photo import ProductPhoto
from product.models.category import Category
from product.forms import ProductForm, CategoryForm
from product.models.product_service import ProductService
from product.models.product_set import ProductSet
from product.models.service import Service


@admin.action(description='approve_order')
def approve_order(modeladmin, request, queryset):
    queryset.update(approved=True)


class ProductPhotoAdmin(admin.TabularInline):
    fields = ('image', 'type')
    model = ProductPhoto
    extra = 0


class ProductSetAdmin(admin.TabularInline):
    fields = ('set_product', 'count')
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
    list_display = ("id", "name_ru", "name_kk", "daily_price", "category", "rnh_id")
    prepopulated_fields = {"slug": ("name_ru",)}
    list_filter = ("category", "type")
    search_fields = ('name_ru', 'name_kk', 'description_ru', 'description_kk')
    form = ProductForm
    inlines = (ProductPhotoAdmin, ProductSetAdmin,
               ProductSpecAdmin, ProductServiceAdmin)


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
    list_display = ('id', 'name', 'phone', 'approved', 'start_time', 'end_time', 'total_price')
    actions = [approve_order, ]
    list_filter = ("approved", "start_time", "end_time")
    readonly_fields = ('bag', 'total_time', 'total_price', 'services_price')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name_ru", "name_kk")
    form = CategoryForm


class HiddenAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        return {}


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(UserBag, UserBagAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(ProductPhoto, HiddenAdmin)
admin.site.register(Attribute, HiddenAdmin)
admin.site.register(ProductSet, HiddenAdmin)
admin.site.register(ProductService, HiddenAdmin)
admin.site.register(BotUser)
admin.site.register(ProductAnnouncement)