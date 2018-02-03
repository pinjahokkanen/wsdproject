from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, get_object_or_404
from webapp.templates.forms import SignUpForm, NewGameForm, UserLoginForm
from django.views.generic import View
from django.views.generic.edit import FormView
from webapp.models import Game, Profile




# Create your views here.
def index(request):
    userobj = Profile.objects.get(pk=request.user.id)
    all_games = userobj.developed_games.all()
    for game in all_games:
        print game.name

    return render(request, "webapp/index.html", {'all_games': all_games})

class UserFormView(FormView):

    form_class = UserCreationForm
    template_name = 'signup.html'

    def get(self, request):
        form = SignUpForm()
        return render(request, 'signup.html', {'form': form})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/games/')
        return render(request, 'signup.html', {'form': form})

class LoginView(FormView):
    def post(self, request):
        form = UserLoginForm(request.POST or None)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
        return render(request, 'registration/login.html', {'form': form})



'''
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})
'''

def addgame(request):
    if request.method == 'POST':
        form = NewGameForm(request.POST)
        if form.is_valid():
            game = form.save(commit=False)


            name = form.cleaned_data.get('name')
            description = form.cleaned_data.get('description')
            url = form.cleaned_data.get('url')
            price = form.cleaned_data.get('price')
            #game.developer = request.user TO BE ADDED

            form.save()
            return redirect('/games/')
    else:
        form = NewGameForm()
    return render(request, 'addgame.html', {'form': form})
