
from django.db import models
from user.models.py import Users


class Workouts(models.Model):
    owner = models.ForeignKey('Users', on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=50)
    sport = models.ForeignKey('Sports', on_delete=models.CASCADE)
    lat = models.DecimalField(decimal_places=2, max_digits=4)
    lng = models.DecimalField(decimal_places=2, max_digits=4)
    radius = models.DecimalField(decimal_places=2, max_digits=4)
    duration = models.DecimalField(decimal_places=2, max_digits=4)
    distance = models.DecimalField(decimal_places=2, max_digits=4)
    average_hr = models.DecimalField(decimal_places=2, max_digits=4)
    calories_burned = models.DecimalField(decimal_places=2, max_digits=4)
    average_speed = models.DecimalField(decimal_places=2, max_digits=4)
    workout_effectiveness = models.BooleanField()
# Create your models here.
