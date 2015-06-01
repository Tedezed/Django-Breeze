import os
import string

def auto_rename(ruta_carpeta, name_real, nombre_final):
	lista_filename = str.split(name_real, '.')
	extencion = ''
	for i in lista_filename:
		#Aqui sacara la extencion
		extencion = i
	name_real = string.replace(name_real, ' ', '_')
	name_real = string.replace(name_real, ':', '')
	ruta_file = ruta_carpeta+name_real
	nombre_final = nombre_final+'.'+extencion
	ruta_final = ruta_carpeta+nombre_final
	comando_final = 'mv %s %s' % (ruta_file, ruta_final)
	print comando_final
	os.system(comando_final)
