from django.http import Http404, HttpResponse
from webapp.models import Game, Profile, Highscore
from django.contrib.auth.models import User
from django.views import generic
import json

class IndexView(generic.ListView):
	template_name = 'games/index.html'
	context_object_name = 'all_games'

	def get_queryset(self):
		return Game.objects.all()

# functio versiot benchmarkiksi

#def index(request):
#	all_games = Game.objects.all()
#	return render(request, "games/index.html", {'all_games': all_games})


class DetailView(generic.DetailView):
	model = Game
	template_name = 'games/singlegame.html'

	def highscore(self):
		return Highscore.objects.get(game=self.object, user=self.request.user.profile);


def renderHighScore(request,game_id):

#	highscore = Highscore(game=currentgame, user=profile)
	highscore = 0
	return render(request, "games/highscore.html", {'highscore': highscore})

def savescore(request,game_id):
	currentgame = Game.objects.get(id=game_id)
	profile = request.user.profile
	highscore = Highscore(game=currentgame, user=profile)
	highscore = 0
	return render(request, "games/highscore.html", {'highscore': highscore})

#def singlegame(request, game_id):
#	try:
#		game = Game.objects.get(id=game_id)
#	except Game.DoesNotExist:
#		raise Http404("Game Not Found")
#	return render(request, "games/singlegame.html", {'game': game})

# def orders(request):
#     return render(request, "games/orders.html")
#     # template_name = 'games/orders.html'
