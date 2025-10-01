from rest_framework import serializers
from .models import Player

class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ['id', 'username', 'display_name', 'created_at', 'is_active']
        read_only_fields = ['id', 'created_at']