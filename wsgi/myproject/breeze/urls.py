from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth.views import login, logout
from . import views

urlpatterns = patterns('',
	#Ejemplos de url:
	#
	#127.0.0.1:8000
  #url(r'^$', views.home, name='home'),
  #127.0.0.1:8000/dir/
  #url(r'^dir/$', views.dir, name='dir'),
  #127.0.0.1:8000/75/numero/
  #url(r'^(?P<numero>[0-9]+)/numero/$', views.numero, name='numero'),
  #127.0.0.1:8000/hola/pepe/
  #url(r'^hola/(?P<nombre>.*)/$', views.hola, name='hola'),
  #127.0.0.1:8000/pepe/template/
  #url(r'^(?P<nombre>.*)/template/$', views.template, name='template'),
  #url(r'^(?P<codigo>[0-9]+)/db/$', views.db_example, name='db_example'),
  #
  #Breeze urls:
  #
  #Index
  url(r'^$', views.index, name='index'),
  url(r'^registro/$', views.signup, name='signup'),
  #Dos formas de Login
  #url(r'^login/$', login, {'template_name': 'login.html', }, name="login"),
  url(r'^login/$', views.login_view, name="login"),
  #url(r'^logout/$', logout, {'template_name': 'index.html', }, name="logout"),
  url(r'^logout/$', views.logout_view, name="logout"),
  url(r'^home/$', views.home, name='home'),
  url(r'^generador/$', views.generador, name="generador"),
  #DEBUG
  url(r'^name/$', views.name, name="name"),
  url(r'^busqueda/$', views.busqueda, name='busqueda'),
  url(r'^partitura/(?P<p_id>[0-9]+)$', views.mostrar_partitura, name='mostrar_partitura'),
  url(r'^uploads/$', views.upload_file, name="uploads"),

)
