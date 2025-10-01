from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Max
from scores.models import Score

class GameLeaderboard(APIView):
    def get(self, request, game_pk):
        qs = (
            Score.objects.filter(game_id=game_pk)
            .values('player__id', 'player__display_name')
            .annotate(best_score=Max('value'))
            .order_by('-best_score')[:10]
        )
        return Response(list(qs))