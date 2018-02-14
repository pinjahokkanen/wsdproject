from django.http import Http404, HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, render, get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse
from django.template import RequestContext
from webapp.models import Game, Profile, GameState, Order
from django.views import generic

from django.shortcuts import redirect

from django.db.models import Count
from django.contrib import messages
from decimal import Decimal
from hashlib import md5
import datetime
import json

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User

from django.shortcuts import render
from .forms import CartForm

from django.views.decorators.csrf import csrf_exempt #TEMPORARELY
from django.contrib.auth.decorators import user_passes_test


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
        return GameState.objects.get(game=self.object, user=self.request.user.profile);




def renderHighScore(request,game_id):

#   highscore = Highscore(game=currentgame, user=profile)
    highscore = 0
    return render(request, "games/highscore.html", {'highscore': highscore})

#NOTE! CSRF NEEDS TO BE IMPLEMENTED

@csrf_exempt
def savescore(request, pk):
    #highscore = request.GET.get('score', None)
    data = json.loads(request.POST.get('jsondata', None))
    print(type(data))
    highscore = data['score']
    #Alternative?: data = { 'scored score': highscore.score }
    print(highscore)

    scoreobj = GameState.objects.get(game=Game.objects.get(pk=pk), user=request.user.profile)
    print(scoreobj)
    if scoreobj.score < highscore:
        scoreobj.score = highscore
        scoreobj.save()
        return HttpResponse(highscore)
    else:
    #   highscore = scoreobj.score
        raise Http404("You didn't score high enough")
    #return render(request, "games/highscores.html", {'highscore': highscore})

@csrf_exempt
def savestate(request, pk):

    data = json.loads(request.POST.get('jsondata', None))
    print(type(data))

    state = data['gameState']
    stateobj = GameState.objects.get(game=Game.objects.get(pk=pk), user=request.user.profile)

    stateobj.state = json.dumps(state)
    stateobj.save()
    print('GAMESTATE SAVED SUCCESSFULLY!')

    score = data['gameState']['score']
    if stateobj.score < score:
        stateobj.score = score
        stateobj.save()
        print('vaihtoehto1')
        return HttpResponse(json.dumps(state), content_type='application/json')
    else:
        del state['score']
        print(state)
        return HttpResponse(json.dumps(state), content_type='application/json')

    #stateobj.state = json.dumps(state)
    #stateobj.save()
    #return HttpResponse(status=200)


    #   highscore = scoreobj.score
    #    raise Http404("You didn't score high enough")
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

        ## For adding games to cart ##
        if form.cleaned_data['action'] == 'add':

            sessioncart = request.session.get('cart_items',[])

            if form.cleaned_data['game'].id in sessioncart:
                jsondata['error'] = "Cart already contains this game"

            #Succesful request
            if jsondata['error'] is None:
                sessioncart.append(form.cleaned_data['game'].id)
                request.session['cart_items'] = sessioncart
                # redirect("games:cart")

        ## For removing games from cart ##
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


def orders(request):
    if request.method == 'GET':

        orders = Order.objects.filter(player=request.user.profile)
        return render(request, 'games/orderlist.html', {'user': request.user, 'orders': orders})

    elif request.method == 'POST':

        game_ids = request.session.get('cart_items', [])
        total = Decimal(0.0)
        queryset = Game.objects.filter(id__in=game_ids)

        # Check for duplicates in user inventory
        for game in queryset:
            # if request.user.profile.games.filter(id__is=game.id).count() > 0:
            #     messages.error(request, "Game already owned. Removing game from the cart.")
            #     game_ids.remove(game.id)
            # else:
                total += game.price

        # Remove concurrent orders of the user
        Order.objects.filter(player=request.user.profile, status="pending").delete()

        queryset = Game.objects.filter(id__in=game_ids)

        if queryset.count() < 1:
            messages.warning(request, "Empty cart! Redirecting...")
            return HttpResponseRedirect(reverse("cart"))

        order = Order.objects.create(player=request.user.profile,
                                    total=total,
                                    orderDate=datetime.datetime.now(),
                                    paymentDate=None,
                                    paymentReference=None,
                                    status='pending')

        for obj in queryset:
            order.games.add(obj)
        # order.games = queryset.all()

        order.save()

        messages.info(request, "Action was succesful.")

        return HttpResponseRedirect(reverse("games:order_details", kwargs={'order_id':order.id}))

    else:
        return HttpResponse(status=405, content="Invalid method.")

def order_details(request, order_id):
    if request.method == 'GET':

        # if order is None:
        #     messsages.error(request, "Invalid order.")
        #     return HttpResponseRedirect(reverse("cart"))

        pid = order_id

        order = None
        try:
            order = Order.objects.get(id=pid)
        except ObjectDoesNotExist:
            messsges.error(request, "Missing or invalid Pid.")
            return HttpResponseRedirect(reverse("cart"))

        if order.player != request.user.profile:
            messsges.error(request, "Not authorized for this order")
            return HttpResponseRedirect(reverse("cart"))

        if order.status != 'error' and order.status != 'pending':
            messages.error(request, "Order status invalid.")
            return HttpResponseRedirect(reverse("cart"))

        # All good
        action = "http://payments.webcourse.niksula.hut.fi/pay/"
        amount = order.total
        sid = "slipsum"  # Fixme Todo: parametrize
        success_url = request.build_absolute_uri(reverse("games:purchase_result"))
        cancel_url = request.build_absolute_uri(reverse("games:purchase_result"))
        error_url = request.build_absolute_uri(reverse("games:purchase_result"))
        secret_key = "277a909c26085600aa111ab18e61a51f"

        checksumstr = "pid={}&sid={}&amount={}&token={}".format(pid, sid, amount, secret_key)

        # checksumstr is the string concatenated above
        m = md5(checksumstr.encode("ascii"))
        checksum = m.hexdigest()
        # checksum is the value that should be used in the payment request

        game_ids = [game.id for game in order.games.all()]

        return render(request, 'games/purchase.html', {'user': request.user,
                                               'cart':  to_cart(game_ids),
                                               'action': action,
                                               'pid': pid,
                                               'sid': sid,
                                               'amount': amount,
                                               'success_url': success_url,
                                               'cancel_url': cancel_url,
                                               'error_url': error_url,
                                               'checksum': checksum})
    else:
        return HttpResponse(status=405, content="Invalid action.")

def purchase_result(request):
    if request.method == 'GET':
        pid = request.GET['pid']
        ref = request.GET['ref']
        result = request.GET['result']
        checksum = request.GET['checksum']

        sid = "slipsum"
        secret_key = "277a909c26085600aa111ab18e61a51f"

        checksumstr = "pid={}&ref={}&result={}&token={}".format(pid, ref, result, secret_key)
        m = md5(checksumstr.encode("ascii"))
        checksum2 = m.hexdigest()

        if checksum != checksum2:
            messages.error(request, "Invalid checksum. Payment not completed.")
            return HttpResponseRedirect(redirect_to=reverse("games:cart"))


        order = None
        try:
            order = Order.objects.get(id=pid)
        except ObjectDoesNotExist:
            messages.error(request, "Invalid OrderId specified. Your payment is invalid.")
            return HttpResponseRedirect(redirect_to=reverse("cart"))

        ## CASES TO CHECK:
        ## [x ] CHECKSUM MATCHES
        ## [ ] STATUS CHECKS OUT
        ## [ ] STATUS IS ALLOWED
        ## [ ] PID IS CORRECT
        ## [ ] USER AUTHORIZED (ORDERS IS USERS)

        if result == "success":
            for item in order.games.all():
                order.player.games.add(item)
            order.player.save()
            order.status = "success"
            order.paymentRefernce = ref
            order.paymentDate = datetime.datetime.now()
            order.save()

            request.session['cart_items'] = []

            return HttpResponseRedirect(redirect_to=reverse("index"))

        ## TO DO: CANCELLED AND ERROR ORDER STATUS

    else:
        return HttpResponse(status=405, content="Invalid method.")
