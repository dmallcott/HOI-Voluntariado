# -*- coding: utf-8 -*-
from django.db import models

class Proyecto(models.Model):

	def __unicode__(self):
	    return unicode(self.titulo)
	    	
	OPCIONES_ESTATUS = (
	('P', 'En proceso'),
	('C', 'Culminado'),
	)


	titulo = models.CharField('Titulo', max_length=30)
	institucion = models.CharField('Institución', max_length=30, blank=True)
	especialidad = models.CharField('Especialidad', max_length=30, blank=True)
	dependencia = models.CharField('Dependencia', max_length=30, blank=True)
	estatus = models.CharField('Estatus', max_length=1, choices=OPCIONES_ESTATUS)
