from django.urls import path
from . import views

urlpatterns = [
    path('', views.allplayers, name = 'allplayers'),
    path('create/', views.createplayer, name = 'player_create'),
    path('<int:id>/edit/', views.updateplayer, name = 'player_update'),
    path('<int:id>/delete/', views.deleteplayer, name = 'player_delete'),
]