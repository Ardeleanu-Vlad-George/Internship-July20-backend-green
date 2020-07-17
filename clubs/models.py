#aplicatia clubs, se vor dezvolta modelele club+event
from django.db import models
from user.models import Users, Sport

#de facut managerii


class Club(models.Model):
    #id - autofield
    #owner - fk catre user
    #name - charfield
    #description - textfield

    owner = models.ForeignKey(Users, on_delete=models.CASCADE)
    name = models.CharField(max_length=31)
    description = models.TextField()
#basic club structure done

class Event(models.Model):
    #id - autofield
    #club -fk catre club
    #name - charfield
    #description - Textfield
    #location - charfield
    #radius - charfield
    #sport - fk catre sport

    organizing_club = models.ForeignKey(Club, on_delete=models.CASCADE)
    name = models.CharField(max_length=31)
    description = models.TextField()
    location = models.CharField(max_length=31)
    radius = models.CharField(max_length=31)
    event_sport = models.ForeignKey(Sport, on_delete=models.CASCADE)
#basic event structure done


# Create your models here.