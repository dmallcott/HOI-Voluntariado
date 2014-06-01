# -*- coding: utf-8 -*-
from django.db import models

class Voluntario(models.Model):
	OPCIONES_GENERO = (
		('M', 'Masculino'),
		('F', 'Femenino'),
	)

	OPCIONES_ESTADO_CIVIL = (
		('C', 'Casado'),
		('S', 'Soltero'),
		('D', 'Divorciado'),
		('V', 'Viudo'),
	)

	OPCIONES_INSTRUCCION = (
		('P', 'Educación Primaria'),
		('M', 'Educación Media'),
		('S', 'Educación Superior'),
	)

	primer_nombre = models.CharField(max_length=30)
	apellido = models.CharField(max_length=30, null=True, blank=True)
	lugar_nacimiento = models.CharField(max_length=30, null=True, blank=True)
	fecha_nacimiento = models.DateField(auto_now_add=True, blank=True)
	edad = models.PositiveIntegerField()
	genero = models.CharField(max_length=1, choices=OPCIONES_GENERO)
	CI = models.CharField(max_length=10, primary_key=True, blank=True)
	estado_civil = models.CharField(max_length=1, choices=OPCIONES_ESTADO_CIVIL)
	direccion = models.CharField(max_length=120, null=True, blank=True)
	telefono_casa = models.PositiveIntegerField(max_length=20)
	telefono_celular = models.PositiveIntegerField(max_length=20)
	grado_instruccion = models.CharField(max_length=1, choices=OPCIONES_INSTRUCCION)
	ocupacion = models.CharField(max_length=30,null=True, blank=True)
	correo_electronico = models.EmailField()









