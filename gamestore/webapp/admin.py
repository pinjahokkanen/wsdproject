from django.contrib import admin
from .models import Profile, Game, GameState, Order

admin.site.register(Profile)
admin.site.register(Game)
admin.site.register(GameState)
admin.site.register(Order)
# Register your models here.
