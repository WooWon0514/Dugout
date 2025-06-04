from django.db import models

class Team(models.Model):
    name = models.CharField(max_length=50, unique=True)
    wins = models.IntegerField()
    losses = models.IntegerField()
    draws = models.IntegerField()

    highlights = models.JSONField(default=dict)
    matchups = models.JSONField(default=dict)
    waa = models.JSONField(default=dict)

    def __str__(self):
        return self.name

class TeamStat(models.Model):
    team = models.OneToOneField('Team', on_delete=models.CASCADE)
    batting_avg = models.FloatField(null=True)
    homeruns = models.IntegerField(null=True)
    hits = models.IntegerField(null=True)
    stolen_bases = models.IntegerField(null=True)
    ops = models.FloatField(null=True)
    era = models.FloatField(null=True)
    whip = models.FloatField(null=True)
    strikeouts = models.IntegerField(null=True)

class VersusRecord(models.Model):
    team = models.ForeignKey('Team', on_delete=models.CASCADE, related_name='versus')
    opponent = models.CharField(max_length=50)
    wins = models.IntegerField()
    draws = models.IntegerField(default=0)
    losses = models.IntegerField()
    win_rate = models.FloatField()

class TeamWAR(models.Model):
    team = models.OneToOneField('Team', on_delete=models.CASCADE)
    pitcher = models.FloatField()
    hitter = models.FloatField()
    bench = models.FloatField()
    defense = models.FloatField()