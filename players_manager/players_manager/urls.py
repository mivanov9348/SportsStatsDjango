from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', lambda request: redirect('players/', permanent=True)),
    path("players/", include('players.urls')),
    path("teams/",include('teams.urls'))
]
