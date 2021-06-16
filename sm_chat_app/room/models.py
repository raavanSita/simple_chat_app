from django.db import models
from datetime import  datetime
# Create your models here.

class Room(models.Model):
    name = models.CharField(max_length=200)

class Message(models.Model):
    value = models.CharField(max_length=500)
    date_created = models.DateTimeField(default=datetime.now)
    user = models.CharField(max_length=500)
    room = models.CharField(max_length=1000) 
