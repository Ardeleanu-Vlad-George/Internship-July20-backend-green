from django.db import models

class Sports(models.Model):
    Running = 0
    Cicling = 1
    TeamSports = 2
    WeightLifting = 3
    TYPES = (
        (0, Running),
        (1, Cicling),
        (2, TeamSports),
        (3, WeightLifting),
    )
    type = models.IntegerField(default=Running, choices=TYPES)