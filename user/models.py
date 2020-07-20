from django.core.exceptions import MultipleObjectsReturned
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


class Users(AbstractUser):
    ADMIN = 0
    COACH = 1
    ATHLETE = 2
    ROLES = (
        (ADMIN, "ADMIN"),
        (COACH, "COACH"),
        (ATHLETE, "ATHLETE"),
    )


    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(blank=True, unique=True)
    USERNAME_FIELD = 'email'
    password = models.CharField(max_length=100)
    role = models.IntegerField(default=ATHLETE, choices=ROLES)
    height = models.DecimalField(decimal_places=2, max_digits=4, blank=True, null=True)
    weight = models.DecimalField(decimal_places=2, max_digits=3, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    REQUIRED_FIELDS = []
    def __str__(self):
        return self.first_name + self.last_name


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
