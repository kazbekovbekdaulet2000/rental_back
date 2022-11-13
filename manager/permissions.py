from rest_framework import permissions


class IsStatisticManager(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm('manager.ManagerStat')

    def has_object_permission(self, request, view, obj):
        return request.user.has_perm('manager.ManagerStat')
