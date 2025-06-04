from django.shortcuts import render
from .models import Team

def team_list(request):
    teams = Team.objects.all().order_by('-wins')  # 예: 승수 기준 정렬
    return render(request, 'teams/team_list.html', {'teams': teams})

from django.shortcuts import render
from .utils import fetch_team_data

def kia_team_detail(request):
    team_data = fetch_team_data(team_code='2002', year=2025)
    return render(request, 'teams/kia_team_detail.html', {'team': team_data})

# teams/views.py

from django.shortcuts import redirect
from .utils import fetch_all_teams_data, save_team_data

def sync_teams(request):
    team_data = fetch_all_teams_data()
    save_team_data(team_data)
    return redirect('team_list')