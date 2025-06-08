from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def main_page(request):
    return render(request, 'main/main.html')

@login_required
def player_ranking(request):
    return render(request, 'players/player_rankings.html')

@login_required
def team_info(request):
    return render(request, 'teams/team_list.html')