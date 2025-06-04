from django.shortcuts import render
from .models import Player

def player_rankings(request):
    rankings = Player.objects.order_by('-views')[:20]
    return render(request, 'players/player_rankings.html', {
        'rankings': rankings
    })