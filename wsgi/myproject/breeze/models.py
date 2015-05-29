from django.db import models

# Create your models here.
from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User

#Modelo de ejemplo
class tabla_ejemplo (models.Model):  
	codigo = models.IntegerField(max_length = 10)
	text = models.CharField(max_length = 140)
	unique_together = (('codigo'),)

#Modelos Breeze
class usuario (models.Model):  
    user = models.OneToOneField(User)
    #Otros campos para usuario django
    correo = models.CharField(max_length = 200)
    cod_avatar = models.CharField(max_length = 50)
    unique_together = (('user'),)

class instrumento (models.Model):
	codigo = models.IntegerField(max_length = 10)
	nombre = models.CharField(max_length = 50)
	unique_together = (('codigo', 'nombre'),)

class partitura (models.Model):
	codigo = models.IntegerField(max_length = 10)
	codigo_usuario = models.ForeignKey(usuario)
	codigo_instrumento = models.ForeignKey(instrumento)
	nombre = models.CharField(max_length = 70)
	visitas = models.IntegerField(max_length = 50)
	archivo_partitura = models.FileField(upload_to='.')
	fecha_publicacion = models.DateTimeField(auto_now_add=True)
	unique_together = (('codigo', 'nombre'),)

class comentario (models.Model):
	codigo = models.IntegerField(max_length = 10)
	codigo_usuario = models.ForeignKey(usuario)
	codigo_partitura = models.ForeignKey(partitura)
	text_comentario = models.CharField(max_length = 140)
	fecha_publicacion = models.DateTimeField(auto_now_add=True)
	unique_together = (('codigo'),)

class valoracion (models.Model):
	codigo = models.IntegerField(max_length = 10)
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