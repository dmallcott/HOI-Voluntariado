# -*- coding: utf-8 -*-
from django.db import models
from apps.voluntariado.models import Voluntario, Proyecto, Servicio


class Proyectos(models.Model):
    proyecto = models.ForeignKey(Proyecto)
    voluntario = models.ForeignKey(Voluntario)
    horas = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = "Proyecto"
        verbose_name_plural = "Proyectos"

    def __unicode__(self):
        return unicode(self.proyecto.titulo)


class Servicios(models.Model):
    servicio = models.ForeignKey(Servicio)
    voluntario = models.ForeignKey(Voluntario)
    horas = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = "Servicio"
        verbose_name_plural = "Servicios"

    def __unicode__(self):
        return unicode(self.servicio.servicio)
