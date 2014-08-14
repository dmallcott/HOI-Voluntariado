# -*- coding: utf-8 -*-
from django.db import models
from apps.voluntarios.models import Voluntario


class Proyecto(models.Model):

    OPCIONES_ESTATUS = (
        ('P', 'En proceso'),
        ('C', 'Culminado'),
    )

    titulo = models.CharField('Titulo', max_length=30)
    institucion = models.CharField('Institución', max_length=30, blank=True)
    especialidad = models.CharField('Especialidad', max_length=30, blank=True)
    dependencia = models.CharField('Dependencia', max_length=30, blank=True)
    estatus = models.CharField(
        'Estatus', max_length=1, choices=OPCIONES_ESTATUS)

    def __unicode__(self):
        return unicode(self.titulo) + " " + unicode(self.institucion)


class ProyectoVoluntario(models.Model):
    proyecto = models.ForeignKey(Proyecto)
    voluntario = models.ForeignKey(Voluntario)
    horas = models.PositiveIntegerField(default=0)

    def __unicode__(self):
        return unicode(self.proyecto.titulo)

    class Meta:
        verbose_name = "Proyecto/Voluntario"
        verbose_name_plural = "Proyectos/Voluntarios"
