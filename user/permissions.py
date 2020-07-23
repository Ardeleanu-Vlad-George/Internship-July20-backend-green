from rest_framework.permissions import BasePermission
from user.models import Users

class IsAdmin(BasePermission):
    def has_admin_permission(self, request, view):
        return Users.ADMIN == request.user

class IsCoach(BasePermission):
    def has_coach_permission(self, request, view):
        return Users.COACH == request.user

class IsAthlete(BasePermission):
    def has_athlete_permission(self, request, view):
        return Users.ATHLETE == request.user

class IsAdminCoach(BasePermission):
    def has_admin_coach_permission(self, request, view):
        return Users.ADMIN == request.user or Users.COACH == request.user




