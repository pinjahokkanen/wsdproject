from django.urls import path
from django.urls import re_path
from . import views


urlpatterns = [
	re_path(r'^$', views.index, name='index'),

	re_path(r'^(?P<game_id>[0-9]+)/$', views.singlegame, name='singlegame'),




]





