"""
URL configuration for leaderboard_api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.http import JsonResponse
import json  # 👈 Added for pretty formatting

from category.views import CategoryViewSet
from games.views import GameViewSet
from players.views import PlayerViewSet
from scores.views import ScoreViewSet
from leaderboard.views import GameLeaderboard

# Initialize router
router = DefaultRouter()
router.register(r'categories', CategoryViewSet, basename='categories')
router.register(r'games', GameViewSet, basename='games')
router.register(r'players', PlayerViewSet, basename='players')
router.register(r'scores', ScoreViewSet, basename='scores')

# 👇 Pretty JSON Welcome View
def welcome(request):
    data = {
        "status": "success",
        "message": "Welcome to Virtual Gaming Leaderboard API!",
        "description": "This API powers a Virtual Gaming Leaderboard system for managing games, players, categories, and scores.",
        "available_endpoints": {
            "Categories": "/api/categories/",
            "Games": "/api/games/",
            "Players": "/api/players/",
            "Scores": "/api/scores/",
            "Game Leaderboard": "/api/games/<game_id>/leaderboard/"
        },
        "auth": {
            "Login / Logout (Browsable API)": "/api-auth/"
        },
        "admin": "/admin/"
    }

    # Use `json.dumps` to format with indentation
    response = json.dumps(data, indent=4, ensure_ascii=False)
    return JsonResponse(json.loads(response), safe=False, json_dumps_params={'indent': 4})

urlpatterns = [
    path('', welcome),  # 👈 Root route for pretty JSON welcome message
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('api/games/<int:game_pk>/leaderboard/', GameLeaderboard.as_view()),
]

