from django.urls import path
from django.urls import re_path
from . import views

app_name = 'developer'


urlpatterns = [
	# Developed games
	re_path(r'^$', views.IndexView.as_view(), name='index'),

	# Single developed game
	re_path(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='developedgame'),

	# /developer/add
	re_path(r'^add/$', views.GameCreate.as_view(), name='game-add'),

	# /developer/[id]/update
	re_path(r'^(?P<pk>[0-9]+)/update/$', views.GameUpdate.as_view(), name='game-update'),

	# # /developer/[id]/delete
	re_path(r'^(?P<pk>[0-9]+)/delete/$', views.GameDelete.as_view(), name='game-delete'),


]
