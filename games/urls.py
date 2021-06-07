from django.urls import path
from games.views import home, GamelistView, GameDetailView ,Game_list,  registry

urlpatterns = [
    path('', GamelistView.as_view(), name="home"),
    # path('<slug:slug>/', Game_Detail , name="game_detail"),

]
