# kbo/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('overview/', views.team_rankings_view, name='kbo_overview'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('players/', views.player_list, name='player_list'),
    path('players/new/', views.player_create, name='player_create'),
]

path('teams/<int:team_id>/', views.team_detail, name='team_detail'),
from django.urls import path
from . import views

urlpatterns = [
    path('players/', views.player_list_view, name='player_list'),
    path('players/create/', views.player_create_view, name='player_create'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('players/', views.player_list_view, name='player_list'),
    path('players/register/', views.register_player, name='register_player'),
]