from django.http import Http404, HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from webapp.models import Game, Profile, Highscore
from django.contrib.auth.models import User
from django.views import generic

from django.contrib.auth.mixins import LoginRequiredMixin

from django.shortcuts import render
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt #TEMPORARELY


class IndexView(LoginRequiredMixin, generic.ListView):
	template_name = 'games/index.html'
	context_object_name = 'all_games'

	def get_queryset(self):
		return Game.objects.all()

# functio versiot benchmarkiksi

#def index(request):
#	all_games = Game.objects.all()
#	return render(request, "games/index.html", {'all_games': all_games})


class DetailView(LoginRequiredMixin, generic.DetailView):
	model = Game
	template_name = 'games/singlegame.html'


	def highscore(self):
		user = self.request.user	
		return Highscore.objects.get(game=self.object, user=self.request.user.profile);




def renderHighScore(request,game_id):

#	highscore = Highscore(game=currentgame, user=profile)
	highscore = 0
	return render(request, "games/highscore.html", {'highscore': highscore})

@csrf_exempt
def savescore(request, pk):
	#highscore = request.GET.get('score', None)
	data = json.loads(request.POST.get('jsondata', None))
	highscore = data['score']
	#Alternative?: data = { 'scored score': highscore.score }

	scoreobj = Highscore.objects.get(game=Game.objects.get(pk=pk), user=request.user.profile)
	if scoreobj.score < highscore:
		scoreobj.score = highscore
		scoreobj.save()
		return HttpResponse(highscore)
	else:
	#	highscore = scoreobj.score
		return Http404("You didn't score high enough")
	#return render(request, "games/highscores.html", {'highscore': highscore})

#def singlegame(request, game_id):
#	try:
#		game = Game.objects.get(id=game_id)
#	except Game.DoesNotExist:
#		raise Http404("Game Not Found")
#	return render(request, "games/singlegame.html", {'game': game})

# def orders(request):
#     return render(request, "games/orders.html")
#     # template_name = 'games/orders.html'
