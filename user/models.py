from django.core.exceptions import MultipleObjectsReturned
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _


class Users(AbstractUser):
    username = None
    ADMIN = 0
    COACH = 1
    ATHLETE = 2
    ROLES = (
        (ADMIN, "ADMIN"),
        (COACH, "COACH"),
        (ATHLETE, "ATHLETE"),
    )
    MALE = 0
    FEMALE = 1
    GENDER = (
        (MALE, "MALE"),
        (FEMALE, "FEMALE"),
    )
    gender = models.IntegerField(default=MALE, choices=GENDER)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    USERNAME_FIELD = 'email'
    password = models.CharField(max_length=100)
    role = models.IntegerField(default=ATHLETE, choices=ROLES)
    height = models.DecimalField(decimal_places=1, max_digits=5, blank=True, null=True)
    weight = models.DecimalField(decimal_places=1, max_digits=5, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.first_name + self.last_name


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError(_('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)