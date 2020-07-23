from django.urls import path
from django.conf.urls import url, include
from . import views

urlpatterns = [
    path('', views.events_list),
    path('event/<int:pk>/', views.delete_event),
]
