from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate

from ..models import Game

'''
class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    developer = forms.BooleanField()
    #print(developer)
    #print('develoewcper 1')
    #if developer:
    #	user.has_perm('webapp.add_game')
    #	user.has_perm('change_game')
    #	user.has_perm('add_game')	

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'developer', 'email')
'''
   
class SignUpForm(forms.ModelForm):
 	password = forms.CharField(widget=forms.PasswordInput)
 	developer = forms.BooleanField(required=False)

 	class Meta:
 		model = User
 		fields = ['username', 'password', 'email']
 		# Developer should be also on this list


class NewGameForm(forms.ModelForm):

	class Meta:
		model = Game
		fields = ('url', 'name', 'description', 'price', 'developer')

		
class UserLoginForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput)

	def clean(self, *args, **kwargs):
		username = form.cleaned_data.get('username')
		password = form.cleaned_data.get('password1')
		user = authenticate(username=username, password=raw_password)


		if username and password:
			
			user = authenticate(username=username, password=raw_password)
			
			if not user:
				raise forms.ValidationError("This user does not exist")

			if not user.check_password(password):
				raise forms.ValidationError("Incorrect password")

			if not user.is_active:
				raise forms.ValidationError("This user is not longer active")
			return super(UserLoginForm, self).clean(*args, **kwargs)












