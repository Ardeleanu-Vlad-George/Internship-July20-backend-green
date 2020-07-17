from django.db import models
from user.models import Users, Sport

# Create your models here.

class Club(models.Model):
    #id - autofield
    #owner - fk to user
    #name - charfield
    #description - textfield
    owner = models.ForeignKey(Users, on_delete=models.CASCADE())
    name = models.CharField(max_length=51)
    description = models.TextField()
