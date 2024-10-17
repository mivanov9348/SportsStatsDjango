from django.urls import path
from . import views

urlpatterns = [
    path('', views.allplayers, name = 'allplayers'),
    path('create/', views.createplayer, name = 'player_create'),
    path('add-random/',views.add_random_player,name='add_random_player'),
    path('<int:id>/edit/', views.updateplayer, name = 'player_update'),
    path('<int:id>/delete/', views.deleteplayer, name = 'player_delete'),
    ]