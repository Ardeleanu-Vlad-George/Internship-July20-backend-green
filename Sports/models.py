from django.db import models


class Sports(models.Model):

    type = models.CharField(max_length=50)

