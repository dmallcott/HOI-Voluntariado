from django.db import models

class Servicio(models.Model):

	def __unicode__(self):
		return unicode(self.servicio)
	
	OPCIONES_TURNO = (
	('am', 'A.M.'),
	('pm', 'P.M.'),
	)


	servicio = models.CharField('Servicio', max_length=30)
	turno = models.CharField('Turno', max_length=2, choices=OPCIONES_TURNO)