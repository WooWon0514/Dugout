from django.urls import path
from .views import player_rankings

urlpatterns = [
    path('rankings/', player_rankings, name='player_rankings'),
]