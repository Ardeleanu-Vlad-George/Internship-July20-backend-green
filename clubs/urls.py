from clubs.views import new_club, all_clubs
from django.urls import path
from rest_framework.authtoken import views

urlpatterns = [
    path('', all_clubs),
    path('create_club/', new_club)
]
