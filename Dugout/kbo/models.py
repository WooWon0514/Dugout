from django.db import models

class Team(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Player(models.Model):
    POSITION_CHOICES = [
        ('P', 'Pitcher'),
        ('C', 'Catcher'),
        ('IF', 'Infielder'),
        ('OF', 'Outfielder'),
    ]

    name = models.CharField(max_length=100)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    position = models.CharField(max_length=2, choices=POSITION_CHOICES)
    games_played = models.PositiveIntegerField(default=0)
    batting_average = models.FloatField(default=0.0)
    home_runs = models.PositiveIntegerField(default=0)
    rbi = models.PositiveIntegerField(default=0)