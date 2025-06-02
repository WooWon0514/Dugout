from django.shortcuts import render
from .models import Team

def team_list(request):
    teams = Team.objects.all().order_by('ranking')
    return render(request, 'teams/team_list.html', {'teams': teams})