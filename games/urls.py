from django.urls import path
from games.views import home, GamelistView, GameDetailView
urlpatterns = [
    path('', GamelistView.as_view(), name="home")
    path('<slug:slug>/', GamelistView.as_view(), name="game_detail")
]
