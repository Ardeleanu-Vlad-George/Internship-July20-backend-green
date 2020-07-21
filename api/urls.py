from django.urls import path
from api.users.views import coach
from api.users.views import user_list

urlpatterns = [
    path('coach/', user_list)
]
