# -*- coding: utf-8 -*-
from django.db import models


class Voluntario(models.Model):

    def __unicode__(self):
        return unicode(self.primer_nombre) + ' ' + unicode(self.apellido)

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

    primer_nombre = models.CharField('Nombre', max_length=30)
    apellido = models.CharField('Apellido', max_length=30, blank=True)
    lugar_nacimiento = models.CharField(
        'Lugar de nacimiento', max_length=30, blank=True)
    fecha_nacimiento = models.DateField('Fecha de nacimiento', blank=True)
    genero = models.CharField('Genero', max_length=1, choices=OPCIONES_GENERO)
    CI = models.CharField(
        'Cédula de identidad', max_length=10, primary_key=True, blank=True)
    institucion = models.CharField('Institución', max_length=30, blank=True)
    ocupacion = models.CharField('Ocupación', max_length=30, blank=True)
    estado_civil = models.CharField(
        'Estado civil', max_length=1, choices=OPCIONES_ESTADO_CIVIL)
    direccion = models.CharField(
        'Dirección de habitación', max_length=120, blank=True)
    telefono_casa = models.PositiveIntegerField(
        'Teléfono de habitación', max_length=20)
    telefono_celular = models.PositiveIntegerField(
        'Teléfono celular', max_length=20)
    grado_instruccion = models.CharField(
        'Grado de instrucción', max_length=1, choices=OPCIONES_INSTRUCCION)
    correo_electronico = models.EmailField('Correo electrónico')
