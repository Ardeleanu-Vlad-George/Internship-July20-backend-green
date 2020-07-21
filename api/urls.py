from django.urls import path
from api.users.views import coach

urlpatterns = [
    path('coach/', coach)
]
