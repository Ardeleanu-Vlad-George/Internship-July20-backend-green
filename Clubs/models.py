from django.db import models
from django.db.models import CASCADE
from user.models import Users


class Clubs(models.Model):
    owner = models.ForeignKey(Users, on_delete=CASCADE,blank=True, null=True)
    name = models.CharField(max_length=100)


class ClubUserStatus(models.Model):
    user_id = models.ForeignKey(Users, on_delete=CASCADE)
    club_id = models.ForeignKey(Clubs, on_delete=CASCADE)
    status = models.IntegerField()

