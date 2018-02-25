from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth.models import Group
from webapp.models import Game

from django.contrib.auth import login, authenticate

class NewGameForm(forms.ModelForm):

	class Meta:
		model = Game
		fields = ('url', 'name', 'description', 'price')



## For editing existing games ##
class EditGameForm(forms.Form):
		class Meta:
			model = Game
