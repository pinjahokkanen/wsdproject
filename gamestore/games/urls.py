from django.urls import path
from django.urls import re_path
from . import views

app_name = 'games'


urlpatterns = [
	re_path(r'^$', views.IndexView.as_view(), name='index'),
	re_path(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='singlegame'),
	re_path(r'^(?P<pk>[0-9]+)/savescore', views.savescore, name='savescore'),
	re_path(r'^(?P<pk>[0-9]+)/savestate', views.savestate, name='savestate'),
	re_path(r'^(?P<pk>[0-9]+)/loadstate', views.loadstate, name='loadstate'),
	re_path(r'^cart/', views.cart, name='cart'),
	re_path(r'^orders/$', views.orders, name='orders'),
	re_path(r'^order_details/(?P<order_id>[a-zA-Z0-9]+)/$', views.order_details, name='order_details'),
	re_path(r'^purchase_result/$', views.purchase_result, name='purchase_result'),
]
