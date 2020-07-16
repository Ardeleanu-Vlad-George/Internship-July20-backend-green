from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.contrib.auth.models import AbstractUser


# Create your models here.


class Users(AbstractUser):
    ADMIN = 0
    COACH = 1
    ATHLETE = 2
    ROLES = (
        (0, ADMIN),
        (1, COACH),
        (2, ATHLETE),
    )
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    password = models.CharField(max_length=30)
    role = models.IntegerField(default=ATHLETE, choices=ROLES)
    height = models.DecimalField(decimal_places=2, max_digits=4)
    weight = models.DecimalField(decimal_places=2, max_digits=3)
    age = models.IntegerField()

    def clean_first(self):
        if self.first_name == '':
            raise ValidationError('Empty field')
        if len(self.first_name) > 30:
            raise ValidationError('Enter a correct first name')

    def clean_second(self):
        if self.last_name == '':
            raise ValidationError('Empty field')
        if len(self.last_name) > 30:
            raise ValidationError('Enter a correct first name')

    def clean_email(self):
        if self.email == '':
            raise ValidationError('Empty field')
        if not validate_email(self.email):
            raise ValidationError('Enter a correct email')

    def clean_password(self):
        if self.password == '':
            raise ValidationError('Empty field')
        if len(self.password) < 8:
            raise ValidationError("Password should contain at least 8 characters")

    def clean_role(self):
        if self.role is None:
            raise ValidationError('Empty field')
        if self.role < 0 or self.role.isdigit() is False:
            raise ValidationError('Enter a valid role')

    def clean_age(self):
        if self.age is None:
            raise ValidationError('Empty field')
        if self.age < 0 or self.age > 99 or self.age.isdigit() is False:
            raise ValidationError('Enter a valid age')

    def clean_height(self):
        if self.height is None:
            raise ValidationError('Empty field')
        if self.height < 0 or self.height > 2.5 or self.role.isdigit() is False:
            raise ValidationError('Enter a valid height')

    def clean_weight(self):
        if self.weight is None:
            raise ValidationError('Empty field')
        if self.weight < 0 or self.weight > 150:
            raise ValidationError('Enter a valid weight')
