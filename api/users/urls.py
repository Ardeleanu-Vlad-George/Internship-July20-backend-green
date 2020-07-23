from django.urls import path
from rest_framework.authtoken import views
from user.views import reset_password, registration, invite, check_email

urlpatterns = [
    path('signin/', views.obtain_auth_token),
    path('reset-password/', reset_password),
    path('invite/', invite),
    path('register/validate/', check_email),
    path('register/', registration),

]
