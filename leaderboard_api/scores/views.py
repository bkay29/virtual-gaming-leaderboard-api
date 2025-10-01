from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from .models import Score
from .serializers import ScoreSerializer

class ScoreViewSet(viewsets.ModelViewSet):
    queryset = Score.objects.select_related('player', 'game').all()
    serializer_class = ScoreSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['player', 'game']
    ordering_fields = ['value', 'timestamp']
    ordering = ['-value']  # default: highest scores first