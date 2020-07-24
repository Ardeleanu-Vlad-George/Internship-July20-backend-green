from django.db import models
from django.db.models import CASCADE
from user.models import Users


class Clubs(models.Model):
    owner = models.ForeignKey(Users, on_delete=CASCADE, blank=True, null=True)
    name = models.CharField(max_length=100)


class ClubUserStatus(models.Model):
    REQUEST = 0
    MEMBER = 1
    STATUS = (
        (REQUEST, "REQUEST"),
        (MEMBER, "MEMBER"),
    )
    user = models.ForeignKey(Users, on_delete=CASCADE)
    club = models.ForeignKey(Clubs, on_delete=CASCADE)
    status = models.IntegerField(default=REQUEST, choices=STATUS)
