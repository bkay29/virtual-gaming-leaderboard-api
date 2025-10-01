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


from category.views import CategoryViewSet
from games.views import GameViewSet
from players.views import PlayerViewSet
from scores.views import ScoreViewSet
from leaderboard.views import GameLeaderboard


router = DefaultRouter()
router.register(r'categories', CategoryViewSet, basename='categories')
router.register(r'games', GameViewSet, basename='games')
router.register(r'players', PlayerViewSet, basename='players')
router.register(r'scores', ScoreViewSet, basename='scores')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),  # DRF login/logout for browsable API
    path('api/games/<int:game_pk>/leaderboard/', GameLeaderboard.as_view()),

]
