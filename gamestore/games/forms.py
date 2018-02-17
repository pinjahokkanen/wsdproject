from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth.models import Group
from webapp.models import Game


## For adding and removing games ## 

class CartForm(forms.Form):
	action = forms.ChoiceField(choices=[('add', 'Add'), ('remove', 'Remove')], required=True)
	game = forms.ModelChoiceField(required=True, queryset=None)

	def __init__(self, *args, **kwargs):
		super(CartForm, self).__init__(*args, **kwargs)
		self.fields['game'].queryset = Game.objects.all()