from django.db import models
from teams.models import Team

class Player(models.Model):
    POSITION_CHOICES = [
        ('P', 'Pitcher'),
        ('C', 'Catcher'),
        ('IF', 'Infielder'),
        ('OF', 'Outfielder'),
        ('DH', 'Designated Hitter'),
    ]

    name = models.CharField(max_length=100)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    position = models.CharField(max_length=3, choices=POSITION_CHOICES)
    war = models.FloatField(default=0.0)
    batting_avg = models.FloatField(null=True, blank=True)
    era = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f"{self.name} ({self.team.name})"