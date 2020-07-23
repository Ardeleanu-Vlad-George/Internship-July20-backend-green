from django.urls import path
from django.conf.urls import url, include

urlpatterns = [
    path('coach/', include('api.coach.urls')),
    path('clubs/', include('api.clubs.urls')),
]

