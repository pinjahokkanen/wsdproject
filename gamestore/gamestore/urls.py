"""gamestore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from webapp import views
from django.contrib.auth import views as auth_views

from django.conf.urls.static import static
from django.conf import settings

app_name = 'gamestore'


urlpatterns = [
	#re_path(r'^login/$', auth_views.login, name='login'),
    #re_path(r'^logout/$', auth_views.logout, {'next_page': '/login'},  name='logout'),
    path('accounts/', include('django.contrib.auth.urls')),

    #social media login
    re_path(r'^oauth/', include('social_django.urls', namespace='social')),

    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    re_path(r'^signup/$', views.UserFormView.as_view(), name='signup'),
    re_path(r'^profile/$', views.update_profile, name='profile_update'),

    re_path(r'^games/', include('games.urls'), name='games'),
    re_path(r'^cart/', include('games.urls'), name='cart'),

    re_path(r'^account_activation_sent/$', views.account_activation_sent, name='account_activation_sent'),
    re_path(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),
    re_path(r'^developer/', include('developer.urls'), name='developer'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
