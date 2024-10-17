from django.db import models
from teams.models import Team

# Create your models here.

class Position(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Player(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(default=0)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    team = models.ForeignKey(Team,on_delete=models.CASCADE,related_name='players')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

