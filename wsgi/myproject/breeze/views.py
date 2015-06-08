#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.contrib import auth
from django.contrib.auth.models import User
from forms import UploadForm
from django.conf import settings
from .models import *
from file_rename import *
from funciones import *

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
    text_db = tabla_ejemplo.objects.order_by('codigo')
    #print text_db[0].text
    for i in text_db:
        if i.codigo == int(codigo):
            return HttpResponse(i.text)
    return HttpResponse("No se encontro nada.")

#####################################################################
#Views Breeze:
def index(request):
    titulo = 'Inicio'
    if request.user.is_authenticated():
        # Do something for authenticated users.
        return render(request, 'index2.html', {'user': request.user, 'titulo': titulo,}, context_instance=RequestContext(request))
    else:
        return render(request, 'index2.html', {'titulo': titulo,})

def signup(request):
    if request.method == 'POST':
        #2-Procesar formaulario
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            username = form.cleaned_data["username"]
            #Va la inicio
            #return HttpResponse(form.cleaned_data["username"])
            titulo = 'Registro correcto'
            mensaje = 'Registro correcto del usuario'
            url = '/login/'
            return render(request, 'correcto.html', {'titulo': titulo, 'mensaje':mensaje, 'url':url, 'username': username,})
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

@login_required()
def upload_file(request):
    titulo = 'UpLoad'
    tipo = 'Subir imagen de perfil'
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            username = request.user
            filename = str(username)+'avi'
            usuario.objects.filter(user=username).update(filename = filename, docfile = request.FILES['docfile'])
            #Renombrar imagen
            #filename_real = str(request.FILES['docfile'])
            #auto_rename(settings.MEDIA_ROOT+'/img_avatar/', filename_real, filename)
            #
            #Enviar si es correcto
            titulo = 'Foto correcta'
            mensaje = 'Foto subida correctamente'
            url = '/home/'
            return render(request, 'correcto.html', {'titulo': titulo, 'mensaje':mensaje, 'url':url, 'username': username,})
    else:
        form = UploadForm()
    #tambien se puede utilizar render_to_response
    #return render_to_response('upload.html', {'form': form}, context_instance = RequestContext(request))
    return render(request, 'upload.html', {'titulo':titulo, 'form': form, 'tipo':tipo})


@login_required()
def logout_view(request):
    logout(request)
    # Redirect to a success page.
    return HttpResponseRedirect('/')

@login_required()
def home(request):
    titulo = 'Perfil'
    username = request.user
    user_breeze = usuario.objects.get(user=username)
    usuario_id = user_breeze.id
    select_partitura = partitura.objects.filter(nombre_usuario_id=usuario_id)
    return render(request, 'home2.html', {'titulo': titulo, 'user': request.user, 'select_partitura':select_partitura}, context_instance=RequestContext(request))

@login_required()
def name(request):
    username = request.user
    usuario_db = usuario.objects.get(user=username)
    #usuario_db = usuario.objects.order_by("user")
    return HttpResponse(usuario_db)

@login_required()
def generador(request):
    titulo = 'Generador v.0.1'
    if request.method == 'POST':
        form = request.POST
        #Sacar info del post
        titulo_cancion = form["titulo-part"]
        notas_musicales = form["mem_post"]
        notas_musicales = notas_musicales.replace('NaN','')
        #
        ##Instanciar usuario
        username = request.user
        user_breeze = usuario.objects.get(user=username)
        partitura.nombre_usuario = user_breeze
        usuario_id = user_breeze.id
        ##
        ##Instanciar instrumento
        nom_instrumento = 'TinWhistle'
        instrumen = instrumento.objects.get(nombre=nom_instrumento)
        partitura.nombre_instrumento = instrumen
        instrumento_id = instrumen.id
        ##
        #Guardar en db
        p = partitura(nombre = titulo_cancion,
                    nombre_usuario_id = usuario_id,
                    nombre_instrumento_id = instrumento_id,
                    visitas = 0,
                    pentagrama = notas_musicales)
        username=''
        try:
            p.save()
        except:
            mensaje = 'Error la partitura %s ya existe' % titulo_cancion
            url = '/generador/'
            return render(request, 'correcto.html', {'titulo': titulo, 'mensaje':mensaje, 'url':url, 'username': username,})
        mensaje = 'Partitura enviada correctamente'
        url = '/home/'
        return render(request, 'correcto.html', {'titulo': titulo, 'mensaje':mensaje, 'url':url, 'username': username,})
    else:
        return render(request, 'generador_hd.html', {'titulo':titulo})

def busqueda(request):
    form = request.POST
    entrada = form["entrada"]
    results = partitura.objects.all()
    list_encontrados = []
    for i in results:
        resultado = palabras_clave(i.nombre, entrada)
        if resultado:
            list_encontrados.append(i.id)
    list_resultados = partitura.objects.filter(id__in=list_encontrados)
    titulo = 'Resultados de busqueda'
    return render(request, 'resultado.html', {'titulo':titulo,'list_resultados':list_resultados})

def mostrar_partitura(request, p_id):
    select_partitura = partitura.objects.get(id=p_id)
    titulo = select_partitura.nombre
    return render(request, 'partitura.html', {'titulo':titulo,'select_partitura':select_partitura})