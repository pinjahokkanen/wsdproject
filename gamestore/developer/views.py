from django.http import Http404, HttpResponse, JsonResponse, HttpResponseRedirect, HttpRequest
from django.shortcuts import render_to_response, render, get_object_or_404
from django.urls import reverse, reverse_lazy
from webapp.models import Game, Profile, GameState, Order
from developer.templates.forms import NewGameForm
from django.views import generic
from django.db import models
from django import forms
import datetime

from django.views.generic.edit import UpdateView, DeleteView, CreateView

from django.shortcuts import redirect

import datetime
import json

from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User

from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your views here.
class IndexView(LoginRequiredMixin, generic.ListView):
    template_name = 'developer/index.html'
    context_object_name = 'all_games'

    def get_queryset(self):
        return Game.objects.all()


class DetailView(LoginRequiredMixin, generic.DetailView):
    model = Game
    template_name = 'developer/developedgame.html'

    def statistics(self):
        return Order.objects.filter(status='success', games=self.object)

## Create, edit and delete games
class GameCreate(LoginRequiredMixin,CreateView):
    model = Game
    template_name = 'developer/game_form.html'
    fields = ('url', 'name', 'description', 'price', 'category','img')

    def form_valid(self, form):
        self.object = form.save()
        user = self.request.user

        user.profile.developed_games.add(self.object)

        # Add Game
        user.profile.games.add(self.object)

        # Create game state for the added game
        new_state = GameState(game = self.object, user = user.profile, timestamp = datetime.datetime.now())
        new_state.save()

        ## Add current user as developer
        return HttpResponseRedirect('/developer/')


class GameUpdate(LoginRequiredMixin, UpdateView):
    model = Game
    template_name = 'developer/game_form.html'
    fields = ('url', 'name', 'description', 'price', 'category','img')

class GameDelete(LoginRequiredMixin, DeleteView):
    model = Game
    success_url = reverse_lazy('developer:index')
