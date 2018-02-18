from django.http import Http404, HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, render, get_object_or_404
from django.urls import reverse
from webapp.models import Game, Profile, GameState, Order
from developer.templates.forms import NewGameForm
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
	template_name = 'developer/addgame.html'
	# form_class = addgame
	success_url = '/developer/{{ game.id }}/'

@permission_required('webapp.addgame')
def addgame(request):
    if request.method == 'POST':
        form = NewGameForm(request.POST, initial={'developer': request.user})
        print("Try to add game")
        print(form)
        if form.is_valid():
            print("Form is valid")
            game = form.save(commit=False)
            name = form.cleaned_data.get('name')
            description = form.cleaned_data.get('description')
            url = form.cleaned_data.get('url')
            price = form.cleaned_data.get('price')
            developer = form.cleaned_data.get('developer')
            
            form.save()
            request.user.profile.games.add(game)
            return redirect('/developer/')
        else:
            print(form.errors.as_data())

    else:
        # alert("Adding the game failed. Please try again.")
        form = NewGameForm()
        print("Sanity check")
    return render(request, 'addgame.html', {'form': form})
