from django.contrib import admin
from .models import *


class UserAdmin(admin.ModelAdmin):
    def has_change_permission(self, request, obj=None):
        if(request.user.is_superuser):
            return True
        return False
    list_display = ['email', 'name', 'surname', 'created_at', 'is_staff']
    ordering = ['-created_at']
    readonly_fields = ('email', 'name', 'surname', 'birth_date',
                       'image', 'city', 'description', 'user_type', 'edu_place', 'country')
    list_filter = ['is_staff', 'verified']
    search_fields = ['email', 'name', 'surname']


admin.site.register(User, UserAdmin)