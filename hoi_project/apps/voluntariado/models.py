# -*- coding: utf-8 -*-
from django.db import models


class Organizacion(models.Model):
    nombre = models.CharField('Nombre', max_length=30, blank=True)
    # Aparte del nombre puede ir cualquier informacion que se quiera usar en
    # informes

    class Meta:
        verbose_name_plural = "Organizaciones"

    def __unicode__(self):
        return unicode(self.nombre)

    # https://docs.djangoproject.com/en/dev/ref/contrib/admin/actions/#actions-that-provide-intermediate-pages
    def horas_mes(self):
        """ Genera el reporte de horas mensuales """
        return None

    def horas_anuales(self):
        """ Genera el reporte de horas anuales """
        return None


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

    # Informacion personal del voluntario
    CI = models.CharField('Cédula de identidad',
                          max_length=10, primary_key=True, blank=True)
    primer_nombre = models.CharField('Nombre', max_length=30)
    apellido = models.CharField('Apellido', max_length=30, blank=True)
    lugar_nacimiento = models.CharField('Lugar de nacimiento',
                                        max_length=30, blank=True)
    fecha_nacimiento = models.DateField('Fecha de nacimiento', blank=True)
    genero = models.CharField('Genero', max_length=1, choices=OPCIONES_GENERO)
    ocupacion = models.CharField('Ocupación', max_length=30, blank=True)
    estado_civil = models.CharField('Estado civil', max_length=1,
                                    choices=OPCIONES_ESTADO_CIVIL)
    # Informacion de contacto
    direccion = models.CharField(
        'Dirección de habitación', max_length=120, blank=True)
    telefono_casa = models.PositiveIntegerField(
        'Teléfono de habitación', max_length=20)
    telefono_celular = models.PositiveIntegerField(
        'Teléfono celular', max_length=20)
    correo_electronico = models.EmailField('Correo electrónico')

    # Informacion de la institucion
    institucion = models.ForeignKey(Organizacion, verbose_name='Institución',
                                    blank=True)
    grado_instruccion = models.CharField(
        'Grado de instrucción', max_length=1, choices=OPCIONES_INSTRUCCION)

    def __unicode__(self):
        return unicode(self.primer_nombre) + ' ' + unicode(self.apellido)

    def horas_mes(self):
        """ Genera el reporte de horas mensuales """
        return None

    def horas_anuales(self):
        """ Genera el reporte de horas anuales """
        return None


class Proyecto(models.Model):

    OPCIONES_ESTATUS = (
        ('P', 'En proceso'),
        ('C', 'Culminado'),
    )

    titulo = models.CharField('Titulo', max_length=30)
    especialidad = models.CharField('Especialidad', max_length=30, blank=True)
    dependencia = models.CharField('Dependencia', max_length=30, blank=True)
    estatus = models.CharField('Estatus', max_length=1,
                               choices=OPCIONES_ESTATUS)

    def __unicode__(self):
        return unicode(self.titulo)

    def horas_mes(self):
        """ Genera el reporte de horas mensuales """
        return None

    def horas_anuales(self):
        """ Genera el reporte de horas anuales """
        return None


class Servicio(models.Model):

    OPCIONES_TURNO = (
        ('am', 'A.M.'),
        ('pm', 'P.M.'),
    )

    servicio = models.CharField('Servicio', max_length=30)
    turno = models.CharField('Turno', max_length=2, choices=OPCIONES_TURNO)

    def __unicode__(self):
        return unicode(self.servicio)

    def horas_mes(self):
        """ Genera el reporte de horas mensuales """
        return None

    def horas_anuales(self):
        """ Genera el reporte de horas anuales """
        return None
