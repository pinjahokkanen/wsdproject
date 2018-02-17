from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, get_object_or_404
from webapp.templates.forms import SignUpForm, NewGameForm, UserLoginForm
from django.forms.fields import DateTimeField
from django.views.generic import View
from django.views.generic.edit import FormView
from webapp.models import Game, Profile, GameState
from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required, permission_required






# Create your views here.
def index(request):
    return render(request, "webapp/index.html", {})

class UserFormView(View):

    form_class = SignUpForm
    template_name = 'signup.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():

            user = form.save(commit=False)
            #user.refresh_from_db()

            #get the data
            username = form.cleaned_data['username']
            raw_password = form.cleaned_data['password']
            developer = form.cleaned_data.get('developer')
            email = form.cleaned_data.get('email')
            print(developer)
            #save password
            user.set_password(raw_password)

            user.save()
            if developer:
                profile = user.profile
                profile.developer = True
                profile.save()
                user.user_permissions.add(webapp.add_game, webapp.change_game, webapp.delete_game)

                '''user.has_perm('webapp.add_game')
                user.has_perm('change_game')
                user.has_perm('add_game')'''
            user = authenticate(username=username, password=raw_password)



            if user.is_active:
                login(request, user)
                return redirect('/games/')

            #profile = user.profile TESTAA TÄLLÄ
            #profile.refresh_from_db()
            #print(user.profile)

            #print(developerStatus)
            #print(profile.user)
            #print(profile.developer) oikein False
            #print(form.cleaned_data.get('username')) nimi
            #print(form.cleaned_data['username'])
            #profile.save()

            #email = form.cleaned_data.get('email')


            #if user.profile.developer:
             #   print('its developer')



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
            return redirect('/games/')
        else:
            print(form.errors.as_data())

    else:
        # alert("Adding the game failed. Please try again.")
        form = NewGameForm()
        print("Sanity check")
    return render(request, 'addgame.html', {'form': form})
