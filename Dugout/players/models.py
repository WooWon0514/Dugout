from django.db import models

class PlayerWAR(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=10)
    batting_avg = models.FloatField(null=True, blank=True)
    era = models.FloatField(null=True, blank=True)
    war = models.FloatField(null=True, blank=True)  # 👈 이거 추가!

    def __str__(self):
        return self.name

# players/models.py
from django.db import models

class Player(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=20)
    batting_avg = models.FloatField(null=True, blank=True)
    era = models.FloatField(null=True, blank=True)
    views = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name