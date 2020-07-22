from django.db import models
from Sports.models import Sports
from Clubs.models import Clubs


class Events(models.Model):
    club = models.ForeignKey(Clubs, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=50)
    location = models.CharField(max_length=30)
    radius = models.CharField(max_length=30)
    sport = models.ForeignKey(Sports, on_delete=models.CASCADE)
