from django.db import models

class Team(models.Model):
    name = models.CharField(max_length=50)
    abbreviation = models.CharField(max_length=5)
    wins = models.PositiveIntegerField(default=0)
    losses = models.PositiveIntegerField(default=0)
    draws = models.PositiveIntegerField(default=0)
    ranking = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return self.name