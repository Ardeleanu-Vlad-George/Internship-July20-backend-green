from django.urls import path
from Events.views import events_list
from django.conf.urls import url, include
from . import views
urlpatterns = [
    path('', views.clubs_list)
]
