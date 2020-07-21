import rest_framework.permissions

class IsAuthenticated(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated)

class IsAdminUser(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_staff)

class IsCoachUser(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_staff)