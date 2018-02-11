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

    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    re_path(r'^signup/$', views.UserFormView.as_view(), name='signup'),
    re_path(r'^addgame/$', views.addgame, name='addgame'),
    re_path(r'^games/', include('games.urls'), name='games'),
    # re_path(r'^cart/', include('games.urls'), name='cart'),
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
