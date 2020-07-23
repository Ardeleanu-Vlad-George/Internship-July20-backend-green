from django.urls import path
from api.clubs.views import club, club_pk

urlpatterns = [
    path('', club),
    path('<int:pk>/', club_pk),

]