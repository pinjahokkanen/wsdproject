from django.shortcuts import render
from django.http import Http404
from webapp.models import Game



def index(request):
	all_games = Game.objects.all()
	return render(request, "games/index.html", {'all_games': all_games})

def singlegame(request, game_id):
	try:
		game = Game.objects.get(id=game_id)
	except Game.DoesNotExist:
		raise Http404("Game Not Found")
	return render(request, "games/singlegame.html", {'game': game})










