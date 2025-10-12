from rest_framework import viewsets, filters, status
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.db.models import Sum
from django.shortcuts import get_object_or_404

from .models import Player
from .serializers import PlayerSerializer


class PlayerViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['username', 'display_name']
    ordering_fields = ['username', 'created_at']


# New: lightweight rank endpoint for a player
# URL: /api/players/<int:pk>/rank/
@api_view(['GET'])
def player_rank(request, pk):
    """
    Return the player's global rank (by total score) and the player's total.
    - Computes total score per player across all scores.
    - Ranks players by descending total.
    """
    # Import here to avoid circular import issues during app import time
    try:
        from scores.models import Score
    except Exception:
        return Response(
            {"detail": "Score model not available or scores app not installed."},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

    # Ensure player exists
    player = get_object_or_404(Player, pk=pk)

    # Aggregate total score per player
    totals_qs = Score.objects.values('player').annotate(total=Sum('value')).order_by('-total')

    # If no totals (no scores at all)
    if not totals_qs:
        return Response({"detail": "No scores found in the system."}, status=status.HTTP_404_NOT_FOUND)

    # Build ordered list of player ids and try to find player's rank
    ordered_players = [entry['player'] for entry in totals_qs]

    try:
        rank_index = ordered_players.index(player.id)
        rank = rank_index + 1
        # Find player's total
        player_total = next((entry['total'] for entry in totals_qs if entry['player'] == player.id), 0)
        return Response({
            "player_id": player.id,
            "player_username": getattr(player, 'username', None),
            "rank": rank,
            "total": player_total
        })
    except ValueError:
        # Player exists but has no scores
        return Response(
            {"detail": "Player exists but has no scores (not ranked)."},
            status=status.HTTP_404_NOT_FOUND
        )
