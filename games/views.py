from django.shortcuts import render
from games.models import Game
from django.views.generic import ListView, DetailView

class GamelistView(ListView):
    model = Game
    template_name = "games/game_list.html"
    context_object_name = "game_list"

class GameDetailView(DetailView):
    model = Game
    context_object_name = Game

def home(request):
    # model = Game()
    # model.title = "main"
    # model.price = 14
    # return render(request, "game_list.html", {"model": model})
    return render(request, "games/game_list.html")