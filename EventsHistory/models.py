from django.db import models
from user.models import Users
from Events.models import Events


class EventsHistory(models.Model):
    Pending = 0
    Accepted = 1
    DENIED = 2
    STATUS = (
        (Pending, "PENDING"),
        (Accepted, "ACCEPTED"),
        (DENIED, "DENIED"),
    )
    userId = models.ForeignKey(Users, on_delete=models.CASCADE)
    status = models.IntegerField(default=Pending, choices=STATUS)
    eventId = models.ForeignKey(Events, on_delete=models.CASCADE)

