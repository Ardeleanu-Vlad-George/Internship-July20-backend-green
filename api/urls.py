from django.urls import path, include

urlpatterns = [
    path('coach/', include('api.coach.urls')),
]
