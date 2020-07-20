from django.urls import path
from api.users.views import CoachView

urlpatterns = [
    path('coach/', CoachView.coach)
]
