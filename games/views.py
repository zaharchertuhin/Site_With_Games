from django.shortcuts import render
from games.models import Game, Registry
from django.views.generic import ListView, DetailView

class GamelistView(ListView):
    model = Game
    template_name = "games/game_list.html"
    context_object_name = "game_list"

class GameDetailView(DetailView):
    model = Game
    context_object_name = "game"

def Game_list(request):
    games = Game.objects.all()
    return render(request, "games/home.html", {"game_list":games})

# def Game_Detail(request, slug):
#     game = Game.objects.get(slug=slug)
#     return render(request, "games/game_detail.html", {"game":game})

def home(request):
    # model = Game()
    # model.title = "main"
    # model.price = 14
    # return render(request, "game_list.html", {"model": model})
    return render(request, "games/game_list.html")

def registry(request):
    reg = Registry
    return render(request, "games/game_registry.html")
