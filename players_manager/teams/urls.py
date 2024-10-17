from django.urls import path
from . import views

urlpatterns = [
    path('',views.allteams,name='allteams')
]