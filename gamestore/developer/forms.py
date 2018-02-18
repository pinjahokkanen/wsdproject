from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth.models import Group
from webapp.models import Game


## For adding and removing games ## 

class EditGameForm(forms.Form):
		class Meta:
			model = Game