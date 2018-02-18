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
from django.contrib.sites.shortcuts import get_current_site

from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string

from django.utils.encoding import force_bytes, force_text
from webapp.tokens import account_activation_token







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
            user.is_active = False


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


            current_site = get_current_site(request)
            subject = 'Activate Your Gamestore Account'
            message = render_to_string('account_activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': force_text(urlsafe_base64_encode(force_bytes(user.pk))),
                'token': account_activation_token.make_token(user),
            })
            user.email_user(subject, message)
            return redirect('account_activation_sent')



            #user = authenticate(username=username, password=raw_password)

            #if user.is_active:
            #    login(request, user)
            #    return redirect('/games/')

        
        return render(request, 'signup.html', {'form': form})

def account_activation_sent(request):
    return render(request, 'account_activation_sent.html')

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.profile.email_confirmed = True
        user.save()
        login(request, user)
        return redirect('/')
    else:
        return render(request, 'account_activation_invalid.html')


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
