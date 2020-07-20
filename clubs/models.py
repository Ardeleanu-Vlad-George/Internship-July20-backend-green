
#de facut managerii
from django.db import models
from user.models import Users, Sport

# Create your models here.

class Club(models.Model):
    #id - autofield
    #owner - fk to user
    #name - charfield
    #description - textfield

    owner = models.ForeignKey(Users, on_delete=models.CASCADE)
    name = models.CharField(max_length=31)
    description = models.TextField()
#basic club structure done

"""
class Event(models.Model):
    #id - autofield
    #club - fk to Club
    #name - Charfield
    #description - textfield
    #location - charfield
    #radius - charfield
    #sport - foreignkey

    org_club = models.ForeignKey(Club, on_delete=models.CASCADE)
    name = models.CharField(max_length=51)
    description = models.TextField()
    location = models.CharField(max_length=31)
    radius = models.CharField(max_length=31)
    event_sport = models.ForeignKey(Sport, on_delete=models.CASCADE())
"""