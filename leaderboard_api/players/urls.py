from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PlayerViewSet, player_rank

router = DefaultRouter()
router.register(r'', PlayerViewSet, basename='player')

urlpatterns = [
    path('', include(router.urls)),            # /api/players/ (list, create, etc.)
    path('<int:pk>/rank/', player_rank, name='player-rank'),  # /api/players/{id}/rank/
]
