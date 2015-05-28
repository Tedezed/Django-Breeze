from django.shortcuts import render
from django.http import HttpResponse
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
	return render(request, 'index.html')