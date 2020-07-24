from django.urls import path
from api.clubs.views import club_pk
from Clubs.views import join_club, get_clubs_and_create, get_club_by_user

urlpatterns = [
    path('user/<str:pk>/', get_club_by_user),
    path('<int:pk>/', club_pk),
    path('join/<int:pk>/', join_club),
    path('', get_clubs_and_create)


]