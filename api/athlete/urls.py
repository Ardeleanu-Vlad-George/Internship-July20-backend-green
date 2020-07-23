from django.urls import path
from Events.views import events_list
from django.conf.urls import url, include
from api import athlete
from api.athlete import views

urlpatterns = [
    path('', views.athlete),
    path('edit/<int:pk>/', views.edit_athlete),
    path('create/', views.athlete),
    path('register/', views.register_athlete),
]
