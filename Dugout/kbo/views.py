from django.shortcuts import render
from django.http import HttpResponse

def team_rankings_view(request):
    return HttpResponse("KBO 팀 순위 페이지입니다.")

from django.shortcuts import render, redirect
from .models import Player
from .forms import PlayerForm

def player_list(request):
    players = Player.objects.all()
    return render(request, 'kbo/player_list.html', {'players': players})

def player_create(request):
    if request.method == 'POST':
        form = PlayerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('player_list')
    else:
        form = PlayerForm()
    return render(request, 'kbo/player_form.html', {'form': form})

from django.shortcuts import get_object_or_404

def team_detail(request, team_id):
    team = get_object_or_404(Team, id=team_id)
    players = Player.objects.filter(team=team)
    return render(request, 'kbo/team_detail.html', {
        'team': team,
        'players': players
    })

from django.shortcuts import render, redirect
from .forms import PlayerForm
from .models import Player

def player_create_view(request):
    if request.method == 'POST':
        form = PlayerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('player_list')  # 선수 리스트 페이지로 이동
    else:
        form = PlayerForm()
    return render(request, 'kbo/player_create.html', {'form': form})

def player_list_view(request):
    players = Player.objects.all()
    return render(request, 'kbo/player_list.html', {'players': players})

from django.shortcuts import render
from .models import Player

def player_list_view(request):
    players = Player.objects.all()
    return render(request, 'kbo/player_list.html', {'players': players})

from django.shortcuts import render, redirect
from .forms import PlayerForm

def register_player(request):
    if request.method == 'POST':
        form = PlayerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('player_list')  # 이건 원하는 페이지로 바꿔도 돼요
    else:
        form = PlayerForm()
    return render(request, 'kbo/player_form.html', {'form': form})