from django.urls import path
from Events.views import events_list
from django.conf.urls import url, include
from .users import views

from api.users.views import coach

urlpatterns = [
    path('coach/', coach),
]