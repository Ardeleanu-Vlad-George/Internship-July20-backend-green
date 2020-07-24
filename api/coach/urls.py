from django.urls import path
from api.coach.views import coach, coach_pk, get_coach_clubs

urlpatterns = [
    path('', coach),
    path('<str:pk>', coach_pk),
    path('clubs/<int:pk>/', get_coach_clubs)

]
