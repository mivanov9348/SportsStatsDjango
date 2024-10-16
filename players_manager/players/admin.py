from django.contrib import admin
from .models import Position, Player  # Import your models

admin.site.register(Position)  # Register the Position model
admin.site.register(Player)  # Register the Player model if you want to manage players as well
