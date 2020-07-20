from django.urls import path
from rest_framework.authtoken import views
from user.views import reset_password, registration, invite

urlpatterns = [
    path('signin/', views.obtain_auth_token),
    path('reset-password/', reset_password),
    path('invite/', invite),
    path('register/', registration),
]
