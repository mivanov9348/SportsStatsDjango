import random

from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404

from .models import Player, Position,Team
from .forms import PlayerForm

# Create your views here.
def allplayers(request):
    players = Player.objects.all().order_by('-id')
    return render(request,'players/allplayers.html',{'players':players})

def add_random_player(request):
    if request.method =='POST':
        names = ['John', 'Paul', 'George', 'Ringo', 'Michael', 'Messi', 'Ivan', 'Ronaldo']
        teams = Team.objects.all()
        positions = Position.objects.all()

        name = random.choice(names)
        age = random.randint(18,40)
        position = random.choice(positions)
        team = random.choice(teams)

        Player.objects.create(name=name,age=age,position=position, team=team)

        return redirect('allplayers')

    return redirect('allplayers')

def createplayer(request):
    if request.method =='POST':
        form = PlayerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('allplayers')
    else:
        form = PlayerForm()
    return render(request,'players/player_form.html',{'form':form})

def updateplayer(request,id):
    player = get_object_or_404(Player,id=id)
    if request.method == 'POST':
        form = PlayerForm(request.POST, instance=player)
        if form.is_valid():
            form.save()
            return redirect('allplayers')
    else:
        form = PlayerForm(instance=player)
    return render(request, 'players/player_form.html',{'form':form})

def deleteplayer(request,id):
    player = get_object_or_404(Player, id=id)
    if request.method == 'POST':
        player.is_active = False
        player.save()
        return redirect('allplayers')
    return render(request, 'players/player_confirm_delete.html',{'player':player})
