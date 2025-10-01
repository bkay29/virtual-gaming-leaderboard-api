from rest_framework import serializers
from .models import Score
from players.models import Player
from games.models import Game
from players.serializers import PlayerSerializer
from games.serializers import GameSerializer

class ScoreSerializer(serializers.ModelSerializer):
    player = PlayerSerializer(read_only=True)
    player_id = serializers.PrimaryKeyRelatedField(queryset=Player.objects.all(), source='player', write_only=True)
    
    game = GameSerializer(read_only=True)
    game_id = serializers.PrimaryKeyRelatedField(queryset=Game.objects.all(), source='game', write_only=True)

    class Meta:
        model = Score
        fields = ['id', 'player', 'player_id', 'game', 'game_id', 'value', 'timestamp']
        read_only_fields = ['timestamp']

    def validate_value(self, v):
        if v < 0:
            raise serializers.ValidationError("Score value must be non-negative.")
        return v