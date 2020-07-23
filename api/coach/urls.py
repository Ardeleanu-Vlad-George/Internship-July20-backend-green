from django.urls import path
from api.coach.views import coach, coach_pk

urlpatterns = [
    path('', coach),
    path('<str:pk>', coach_pk)

]
