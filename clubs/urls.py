from clubs.views import new_club
from django.urls import path
from rest_framework.authtoken import views

urlpatterns = [
    path('create_club/', new_club)
]
