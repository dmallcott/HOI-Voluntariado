# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Voluntario.edad'
        db.delete_column(u'voluntarios_voluntario', 'edad')


        # Changing field 'Voluntario.fecha_nacimiento'
        db.alter_column(u'voluntarios_voluntario', 'fecha_nacimiento', self.gf('django.db.models.fields.DateField')())

    def backwards(self, orm):
        # Adding field 'Voluntario.edad'
        db.add_column(u'voluntarios_voluntario', 'edad',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=20),
                      keep_default=False)


        # Changing field 'Voluntario.fecha_nacimiento'
        db.alter_column(u'voluntarios_voluntario', 'fecha_nacimiento', self.gf('django.db.models.fields.DateField')(auto_now_add=True))

    models = {
        u'voluntarios.voluntario': {
            'CI': ('django.db.models.fields.CharField', [], {'max_length': '10', 'primary_key': 'True'}),
            'Meta': {'object_name': 'Voluntario'},
            'apellido': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'correo_electronico': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'direccion': ('django.db.models.fields.CharField', [], {'max_length': '120', 'blank': 'True'}),
            'estado_civil': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'fecha_nacimiento': ('django.db.models.fields.DateField', [], {'blank': 'True'}),
            'genero': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'grado_instruccion': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'lugar_nacimiento': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'ocupacion': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'primer_nombre': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'telefono_casa': ('django.db.models.fields.PositiveIntegerField', [], {'max_length': '20'}),
            'telefono_celular': ('django.db.models.fields.PositiveIntegerField', [], {'max_length': '20'})
        }
    }

    complete_apps = ['voluntarios']