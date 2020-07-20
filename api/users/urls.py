from django.urls import path
from rest_framework.authtoken import views
from user.views import SendEmail

urlpatterns = [
    path('signin/', views.obtain_auth_token),
    path('reset-password/', SendEmail.reset_password),
    path('invite/', SendEmail.invite)
]
