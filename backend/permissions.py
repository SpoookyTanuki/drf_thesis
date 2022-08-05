from rest_framework import permissions


class IsShop(permissions.BasePermission):
    message = 'Страница доступна только для партнёров'

    def has_permission(self, request, view):
        if request.user.type == 'shop':
            return True


class IsAdminOrReadOnly(permissions.BasePermission):
    message = 'Нет прав на внесение изменений'

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return bool(request.user and request.user.is_superuser)

