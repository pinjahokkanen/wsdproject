from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth.models import Group


## For adding and removing games ## 

class CartForm(forms.Form):
	actions = forms.ChoiceField(choices=[('add', 'Add Game'), ('remove', 'Remove Game')], required=True)
	game = forms.ModelChoiceField(required=True, queryset=None)

	def __init__(self, *args, **kwargs):
		super(CartForm, self).__init__(*args, **kwargs)
		self.fields['game'].queryset = Game.objects.all()