from django.urls import path
from django.urls import re_path
from . import views

app_name = 'games'


urlpatterns = [
	re_path(r'^$', views.IndexView.as_view(), name='index'),
	re_path(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='singlegame'),
	re_path(r'^(?P<pk>[0-9]+)/savescore$', views.savescore, name='savescore'),
#	re_path(r'^renderHighScore/(?P<pk>[0-9]+)/$', views.renderHighScore, name='highscore'),
	#re_path(r'^savescore/(?P<pk>[0-9]+)/$', views.savescore, name='savescore'),
	# re_path(r'^orders', views.orders, name='orders'),
]
