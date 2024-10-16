from django import forms
from .models import Player, Position

class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = ['name','age','position','team']