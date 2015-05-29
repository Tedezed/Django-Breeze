from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.contrib import auth
from django.contrib.auth.models import User
from .models import *

#Views de ejemplo
def home(request):
	return HttpResponse("Hello, world. Breeze.")

def dir(request):
	return HttpResponse("dir")

def numero(request, numero):
	return HttpResponse("Tu numero %s" % numero)

def hola(request, nombre):
	return HttpResponse("Hola %s" % nombre)

def template(request, nombre):
	context = {'nombre': nombre}
	return render(request, 'example.html', context)

def db_example(request, codigo):
	#text_db = tabla_ejemplo.objects.raw('SELECT codigo FROM tabla_ejemplo WHERE codigo = %s' % codigo)
	text_db = libros = tabla_ejemplo.objects.order_by('codigo')
	#print text_db[0].text
	for i in text_db:
		if i.codigo == int(codigo):
			return HttpResponse(i.text)
	return HttpResponse("No se encontro nada.")

#Views Breeze:
def index(request):
	titulo = 'Inicio'
	return render(request, 'index.html', {'titulo': titulo,})

def signup(request):
	if request.method == 'POST':
		#2-Procesar formaulario
		form = UserCreationForm(request.POST)
		if form.is_valid():
			new_user = form.save()
			username = form.cleaned_data["username"]
			#Va la inicio
			#return HttpResponse(form.cleaned_data["username"])
			return HttpResponseRedirect('/home/')
		else:
			#Pasar errores
			titulo = 'Registro'
			return render(request, "signup.html", {'form': form, 'titulo': titulo})
	else:
		#1-Envio de formulario
		titulo = 'Registro'
		form = UserCreationForm()
		return render(request, "signup.html", {'form': form, 'titulo': titulo})

@login_required()
def home(request):
    return render_to_response('home.html', {'user': request.user}, context_instance=RequestContext(request))