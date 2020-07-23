from rest_framework.permissions import BasePermission
from user.models import Users

class IsAuthenticate(BasePermission):
    k=Users
    def has_admin_permission(self, request, view, k):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return k.ADMIN == request.user
    def has_coach_permission(self, request, view, k):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return k.COACH == request.user
    def has_athlete_permission(self, request, view, k):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return k.ATHLETE == request.user