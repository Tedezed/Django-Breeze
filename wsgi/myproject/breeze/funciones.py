#!/usr/bin/env python
# -*- coding: utf-8 -*-

def palabras_clave(nombre, entrada):
    entrada = entrada.lower()
    nombre = nombre.lower()
    list_tags = nombre.split(" ")
    for t in list_tags:
        if entrada == t:
            return True