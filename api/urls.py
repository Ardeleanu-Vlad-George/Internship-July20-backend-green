from django.urls import path
<<<<<<< HEAD
from Events.views import events_list
from django.conf.urls import url, include
from .users import views
urlpatterns = [
    path('', views.athlete),
]
=======
from api.users.views import coach

urlpatterns = [
    path('coach/', coach)
]
>>>>>>> 827bf7070bce73d84cc06776d9a40a249405f972
