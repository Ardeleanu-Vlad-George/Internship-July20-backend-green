from django.db import models


class Events(models.Model):
    club = models.ForeignKey('Events', on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=50)
    location = models.CharField(max_length=30)
    radius = models.CharField(max_length=30)
    #s port = models.ForeignKey('Sports', on_delete=models.CASCADE)
