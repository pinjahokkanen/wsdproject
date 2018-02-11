from django.http import Http404, HttpResponse, JsonResponse
from django.shortcuts import render_to_response, render, get_object_or_404
from django.template import RequestContext
from webapp.models import Game, Profile, Highscore
from django.contrib.auth.models import User
from django.views import generic

from django.contrib.auth.mixins import LoginRequiredMixin

from django.shortcuts import render
from .forms import CartForm
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt #TEMPORARELY
from django.contrib.auth.decorators import user_passes_test
from django.core.exceptions import ObjectDoesNotExist

class IndexView(LoginRequiredMixin, generic.ListView):
    template_name = 'games/index.html'
    context_object_name = 'all_games'

    def get_queryset(self):
        return Game.objects.all()

class DetailView(LoginRequiredMixin, generic.DetailView):
    model = Game
    template_name = 'games/singlegame.html'


    def highscore(self):
        user = self.request.user    
        return Highscore.objects.get(game=self.object, user=self.request.user.profile);




def renderHighScore(request,game_id):

#   highscore = Highscore(game=currentgame, user=profile)
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
    #   highscore = scoreobj.score
        return Http404("You didn't score high enough")
    #return render(request, "games/highscores.html", {'highscore': highscore})


def cart(request):
    ## Handle case not logged in

    ## Handle GET
    if request.method == 'GET':
        game_ids = request.session.get('cart_items',[])
        return render(request, 'games/cart.html', {'user':request.user, 'cart': to_cart(game_ids)})

    ## Handle POST

    elif request.method == 'POST':

        if not request.is_ajax():
            messages.error(request, "Only Ajax calls permitted")
            return HttpResponseRedirect(reverse("cart"))

        ## For handling all the error cases
        jsondata = {'error': None}

        # if not user.request.is_active():
        #     jsondata['error'] = "Not a player. Aborted..."
        #     return HttpResponseRedirect(reverse("cart"))

        ## CASES TO DO:
        ## [ ] CLIENT NOT USER
        ## [x] CASE FORM VALID
        ## [ ] CASE NOT AJAX
        ## [x] DUPLICATES 
        ## [ ] GAME ALREADY OWNED BY USER

        form = CartForm(request.POST)

        if not form.is_valid():
            jsondata['error'] = form.errors
            return JsonResponse(status=400, data=jsondata)

        if form.cleaned_data['action'] == 'add':

            sessioncart = request.session.get('cart_items',[])

            if form.cleaned_data['game'].id in sessioncart:
                jsondata['error'] = "Cart already contains this game"

            if jsondata['error'] is None:
                sessioncart.append(form.cleaned_data['game'].id)
                request.session['cart_items'] = sessioncart

        elif form.cleaned_data['action'] == 'remove':
            items = request.session.get('cart_items', [])
            if form.cleaned_data['game'].id in items:
                items.remove(form.cleaned_data['game'].id)
                request.session['cart_items'] = items

        else:
            jsondata['error'] = "Unknown action requested."

        if jsondata['error'] is not None:
            return JsonResponse(status=400, data=jsondata)
        else:
            return JsonResponse(status=201, data=jsondata)

    else:
        return HttpResponse(status=405, content="Invalid action.")



def to_cart(game_ids, user=None):

    result = {}
    result['games'] = []
    result['total'] = 0

    for id in game_ids:
        try:
            game = Game.objects.get(id=id)
            result['total'] += game.price
            result['games'].append(game.to_json_dict(user=user))
        except ObjectDoesNotExist:
            messages.error("Cart element was invalid")
            continue 
    return result


# def order(request):
#     if request.method == 'GET'