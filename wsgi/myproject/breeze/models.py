#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.
from django.contrib import admin
from django.contrib.auth.models import User
from django.db.models.signals import post_save

#Modelo de ejemplo
class tabla_ejemplo (models.Model):  
	codigo = models.IntegerField(max_length = 10)
	text = models.CharField(max_length = 140)
	unique_together = (('codigo'),)
##################

#Modelos Breeze
class usuario (models.Model):  
    user = models.OneToOneField(User)
    #Otros campos para usuario django
    filename = models.CharField(max_length=100)
    docfile = models.FileField(upload_to='img_avatar')
    unique_together = (('user'),)

    def __str__(self):
    	return self.user.username

#Anadir usurio Django a la tabla usuario
def create_user_profile(sender, instance, created, **kwargs):
	if created:
		usuario.objects.create(user=instance)

#Ejecutar para aniadir instancia
post_save.connect(create_user_profile, sender=User)
################################

class instrumento (models.Model):
	nombre = models.CharField(max_length = 50)
	unique_together = (('nombre'),)

	def __str__(self):
		return self.nombre

class partitura (models.Model):
	nombre_usuario = models.ForeignKey(usuario)
	nombre_instrumento = models.ForeignKey(instrumento)
	nombre = models.CharField(max_length = 100)
	visitas = models.IntegerField(max_length = 100, default=0)
	#archivo_partitura = models.FileField(upload_to='.')
	pentagrama = models.CharField(max_length = 900)
	fecha_publicacion = models.DateTimeField(auto_now_add=True)
	unique_together = (('nombre'),)

	def __str__(self):
		return self.nombre

class comentario (models.Model):
	codigo_usuario = models.ForeignKey(usuario)
	codigo_partitura = models.ForeignKey(partitura)
	text_comentario = models.CharField(max_length = 140)
	fecha_publicacion = models.DateTimeField(auto_now_add=True)
	unique_together = (('codigo'),)


class valoracion (models.Model):
	codigo_usuario = models.ForeignKey(usuario)
	codigo_partitura = models.ForeignKey(partitura)
	tipo = models.IntegerField(max_length = 1)
	unique_together = (('codigo'),)


#Registro de panel de admin
admin.site.register(tabla_ejemplo)
admin.site.register(usuario)
admin.site.register(partitura)
admin.site.register(instrumento)
admin.site.register(comentario)
admin.site.register(valoracion)