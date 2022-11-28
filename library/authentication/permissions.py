from rest_framework import permissions


class CustomUserPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            if request.method in permissions.SAFE_METHODS:
                return True


class IsSuperUserOrNotAuthenticate(permissions.BasePermission):
    # def has_permission(self, request, view):
    #     print(not request.user.is_authenticated)
    #     if not request.user.is_authenticated or request.user.is_superuser:
    #         return True
    #
    #     return False

    def has_object_permission(self, request, view, obj):
        print(not request.user.is_authenticated)
        if not request.user.is_authenticated or request.user.is_superuser:
            return True

        return False


class IsOwnerOrStaff(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        print(request.user.is_staff or request.user == obj)
        return request.user.is_staff or request.user == obj


class IsOwnerOrSuperUser(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.is_superuser or request.user == obj


class IsNotAllowed(permissions.BasePermission):
    def has_permission(self, request, view):
        return False
