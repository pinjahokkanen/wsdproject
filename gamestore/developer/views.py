from django.http import Http404, HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, render, get_object_or_404
from django.urls import reverse
from webapp.models import Game, Profile, GameState, Order
from django.views import generic
from django.views.generic import UpdateView

from django.shortcuts import redirect

import datetime
import json

from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User

# Create your views here.
class IndexView(LoginRequiredMixin, generic.ListView):
    template_name = 'developer/index.html'
    context_object_name = 'all_games'

    def get_queryset(self):
        return Game.objects.all()

class DetailView(LoginRequiredMixin, generic.DetailView):
    model = Game
    template_name = 'developer/developedgame.html'

class GameUpdateView(UpdateView):
	model = Game
	template_name = 'webapp/addgame.html'
	# form_class = addgame
	success_url = '/developer/{{ game.id }}/'
