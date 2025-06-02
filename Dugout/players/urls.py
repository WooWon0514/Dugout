from django.urls import path, include
from .views import player_rankings

urlpatterns = [
    path('rankings/', player_rankings, name='player_rankings'),
]

path('players/', include('players.urls'))