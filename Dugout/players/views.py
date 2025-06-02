from django.shortcuts import render
from .models import Player

def player_rankings(request):
    hitters = Player.objects.filter(batting_avg__isnull=False).order_by('-batting_avg')[:10]
    pitchers = Player.objects.filter(era__isnull=False).order_by('era')[:10]
    return render(request, 'players/player_rankings.html', {
        'hitters': hitters,
        'pitchers': pitchers
    })