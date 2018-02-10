from django.contrib import admin

from .models import Profile, Game, Highscore

admin.site.register(Profile)
admin.site.register(Game)
admin.site.register(Highscore)
# Register your models here.
