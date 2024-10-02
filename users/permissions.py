from rest_framework import permissions


class IsLibrarian(permissions.BasePermission):
    """
    Проверяет, является ли пользователь Библиотекарем.
    """

    def has_permission(self, request, view):
        return request.user.groups.filter(name="Библиотекарь").exists()


class IsUser(permissions.BasePermission):
    """
    Проверяет, является ли пользователь обычным пользователем.
    """

    def has_object_permission(self, request, view, obj):
        if request.user == obj:
            return True
        return False
