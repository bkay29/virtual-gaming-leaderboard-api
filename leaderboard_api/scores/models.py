from django.db import models
from players.models import Player
from games.models import Game

# Create your models here.
class Score(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.SET_NULL, null=True, blank=True)
    value = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        indexes = [
            models.Index(fields=['player', 'game']),
        ]
        ordering = ['-timestamp'] # default ordering by latest score

    def __str__(self):
        return f"{self.player.username} - {self.value}"
