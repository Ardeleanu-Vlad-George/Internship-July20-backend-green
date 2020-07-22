from django.db import models
from user.models import Users


class Clubs(models.Model):
    owner = models.ForeignKey(Users, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=30)
    invites = models.CharField(max_length=500)
    requests = models.CharField(max_length=500)
    members = models.CharField(max_length=500)
# Create your models here.
