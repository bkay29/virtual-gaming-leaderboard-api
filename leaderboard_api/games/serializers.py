from rest_framework import serializers
from .models import Game
from category.models import Category  # model import for PrimaryKeyRelatedField
from category.serializers import CategorySerializer

class GameSerializer(serializers.ModelSerializer):
    # Show nested category on reads, accept category id on writes
    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        source='category',
        write_only=True
    )

    class Meta:
        model = Game
        fields = ['id', 'name', 'category', 'category_id', 'created_at']
        read_only_fields = ['id', 'created_at']