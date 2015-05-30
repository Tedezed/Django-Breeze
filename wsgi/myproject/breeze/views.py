from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
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
	if request.user.is_authenticated():
		# Do something for authenticated users.
		return render(request, 'index.html', {'user': request.user, 'titulo': titulo,}, context_instance=RequestContext(request))
	else:
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
			return HttpResponseRedirect('/login/')
		else:
			#Pasar errores
			titulo = 'Registro'
			return render(request, "signup.html", {'form': form, 'titulo': titulo})
	else:
		#1-Envio de formulario
		titulo = 'Registro'
		form = UserCreationForm()
		return render(request, "signup.html", {'form': form, 'titulo': titulo})

def login_view(request):
	titulo = 'Login'
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				login(request, user)
				# Redirect to a success page.
				return HttpResponseRedirect('/home/')
			else:
				# Return a 'disabled account' error message
				#return HttpResponse("Cuenta desactivada.")
				errors = "Cuenta desactivada."
			return render(request, "login.html", {'errors':errors, 'titulo': titulo})

		else:
			# Return an 'invalid login' error message.
			#return HttpResponse("Login erroneo.")
			errors = "Login erroneo."
			return render(request, "login.html", {'errors':errors, 'titulo': titulo})
	else:
		return render(request, "login.html", {'titulo': titulo})

def logout_view(request):
	logout(request)
	# Redirect to a success page.
	return HttpResponseRedirect('/')

@login_required()
def home(request):
    return render_to_response('home2.html', {'user': request.user}, context_instance=RequestContext(request))