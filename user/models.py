from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class Users(AbstractUser):
    ADMIN = 0
    COACH = 1
    ATHLETE = 2
    ROLES = (
        (ADMIN, "ADMIN"),
        (COACH, "COACH"),
        (ATHLETE, "ATHLETE"),
    )
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    password = models.CharField(max_length=30)
    role = models.IntegerField(default=ATHLETE, choices=ROLES)
    height = models.DecimalField(decimal_places=2, max_digits=4)
    weight = models.DecimalField(decimal_places=2, max_digits=3)
    age = models.IntegerField()

class Sport:
    pass