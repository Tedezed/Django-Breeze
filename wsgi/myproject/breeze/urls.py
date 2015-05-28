from django.conf.urls import patterns, include, url
from django.contrib import admin
from . import views

urlpatterns = patterns('',
	#Ejemplos de url:
	#
	#127.0.0.1:8000
    #url(r'^$', views.home, name='home'),
    #127.0.0.1:8000/dir/
    url(r'^dir/$', views.dir, name='dir'),
    #127.0.0.1:8000/75/numero/
    url(r'^(?P<numero>[0-9]+)/numero/$', views.numero, name='numero'),
    #127.0.0.1:8000/hola/pepe/
    url(r'^hola/(?P<nombre>.*)/$', views.hola, name='hola'),
    #127.0.0.1:8000/pepe/template/
    url(r'^(?P<nombre>.*)/template/$', views.template, name='template'),
    url(r'^(?P<codigo>[0-9]+)/db/$', views.db_example, name='db_example'),
    #
   	#Breeze urls:
   	#
   	#Index
   	url(r'^$', views.index, name='index'),
)