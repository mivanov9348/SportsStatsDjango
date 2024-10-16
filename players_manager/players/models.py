from django.db import models

# Create your models here.

class Position(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Player(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(default=0)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    team = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

