from clubs.views import new_club, all_clubs, del_club
from django.urls import path
from rest_framework.authtoken import views

urlpatterns = [
    path('', all_clubs),
    path('create_club/', new_club),
    path('delete_club/', del_club),
    path('<id>/view_club', viw_club)
]
