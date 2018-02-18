from django.urls import path
from django.urls import re_path
from . import views

app_name = 'developer'


urlpatterns = [
	# Developer pages
	re_path(r'^$', views.IndexView.as_view(), name='index'),
	re_path(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='developedgame'),
	re_path(r'^addgame/$', views.addgame, name='addgame'),

]
