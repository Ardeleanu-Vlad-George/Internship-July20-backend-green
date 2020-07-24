from rest_framework.permissions import BasePermission
from user.models import Users


class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return Users.ADMIN == request.user.role


class IsCoach(BasePermission):
    def has_permission(self, request, view):
        return Users.COACH == request.user.role


class IsAthlete(BasePermission):
    def has_permission(self, request, view):
        return Users.ATHLETE == request.user.role


class IsAdminCoach(BasePermission):
    def has_permission(self, request, view):
        return Users.ADMIN == request.user.role or Users.COACH == request.user.role
