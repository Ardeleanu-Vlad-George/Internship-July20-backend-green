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
<<<<<<< HEAD
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    password = models.CharField(max_length=30)
    role = models.IntegerField(default=ATHLETE, choices=ROLES)
    height = models.DecimalField(decimal_places=2, max_digits=4)
    weight = models.DecimalField(decimal_places=2, max_digits=3)
    age = models.IntegerField()

    def first_restriction(self):
        pass
    def clean_first(self):
        if self.first_name == '':
            raise ValidationError('Empty field')
        if len(self.first_name) > 30:
            raise ValidationError('Enter a correct first name')
=======
>>>>>>> 4460cd35eb7783b17432cbe3f3aff8d62050595c

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

<<<<<<< HEAD
    def clean_weight(self):
        if self.weight is None:
            raise ValidationError('Empty field')
        if self.weight < 0 or self.weight > 150:
            raise ValidationError('Enter a valid weight')

class Sport:
    pass
=======
>>>>>>> 4460cd35eb7783b17432cbe3f3aff8d62050595c
