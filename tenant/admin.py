from django.contrib import admin
from django_tenants.admin import TenantAdminMixin
from tenant.models import TenantClient


@admin.register(TenantClient)
class TenantClientAdmin(TenantAdminMixin, admin.ModelAdmin):
    list_display = ('name', 'paid_until')
