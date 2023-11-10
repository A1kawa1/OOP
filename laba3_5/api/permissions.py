from rest_framework import permissions
from django.core.exceptions import PermissionDenied


class AuthorPermissions(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        if request.user != obj.author:
            raise PermissionDenied

        return True
