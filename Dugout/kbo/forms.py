from django import forms
from .models import Player

class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = ['name', 'team', 'position', 'games_played', 'batting_average', 'home_runs', 'rbi']

from django import forms
from .models import Player

from django import forms
from .models import Player

class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = [
            'name',
            'team',
            'position',
            'games_played',
            'batting_average',
            'home_runs',
            'rbi',
        ]