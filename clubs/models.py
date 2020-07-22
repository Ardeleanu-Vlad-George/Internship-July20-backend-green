
#de facut managerii
from django.db import models
from user.models import Users


class Club(models.Model):
    name = models.CharField(max_length=200, unique=True)
    description = models.TextField()

    class Meta:
        pass

    def __str__(self):
        return self.name


class ClubHistory(models.Model):
    #fk user
    #fk club
    #choice field - accept, pending, reject
    ACCEPT = 0
    PENDING = 1
    REJECT = 3

    status = (
        (ACCEPT, "Accepted"),
        (PENDING, "Pending"),
        (REJECT, "Rejected"),
    )

    _usr = models.ForeignKey(Users, on_delete=models.CASCADE)
    _clb = models.ForeignKey(Club, on_delete=models.CASCADE)

    class Meta:
        pass

    def __str__(self):
        return "User: "+self._usr.name + "\nClub: "+self._clb.name
