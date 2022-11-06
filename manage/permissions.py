from rest_framework import permissions
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import Group


class IsStatisticManager(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm('manage.Statistics')

    def has_object_permission(self, request, view, obj):
        return request.user.has_perm('manage.Statistics')
