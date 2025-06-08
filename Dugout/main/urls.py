# main/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name='main'),
    path('players/', views.player_ranking, name='player_ranking'),
    path('teams/', views.team_info, name='team_info'),
]
