from django.urls import path
from Events.views import events_list
from django.conf.urls import url, include
from api import athlete
from api.athlete import views

urlpatterns = [
    path('', views.athlete),
    path('edit/', views.delete_athlete),
    path('athlete/', views.athlete),
    path('create_get/', views.get_athlete),
]
