from django.urls import path
from .views import team_list, kia_team_detail, sync_teams
urlpatterns = [
    path('list/', team_list, name='team_list'),
    path('kia/', kia_team_detail, name='kia_team_detail'),
    path('sync/', sync_teams, name='sync_teams'),
]