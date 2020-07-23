
from django.urls import path
from .views import sport

urlpatterns = [
    path('', sport),
]

