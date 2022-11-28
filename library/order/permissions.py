from rest_framework import permissions


class NotAllowedUpdateAndDeletePermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS and request.user.is_authenticated:
            return True

        if request.method in ('PUT', 'DELETE'):
            return False

        return bool(request.user.is_authenticated and request.user.role == 0)
