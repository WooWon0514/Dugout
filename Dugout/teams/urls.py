from django.urls import path, include
from .views import team_list

urlpatterns = [
    path('', team_list, name='team_list'),
]

path('teams/', include('teams.urls')),