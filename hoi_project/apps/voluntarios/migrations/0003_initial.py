# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Voluntario'
        db.create_table(u'voluntarios_voluntario', (
            ('primer_nombre', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('apellido', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True)),
            ('lugar_nacimiento', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True)),
            ('fecha_nacimiento', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('edad', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('genero', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('CI', self.gf('django.db.models.fields.CharField')(max_length=10, primary_key=True)),
            ('estado_civil', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('direccion', self.gf('django.db.models.fields.CharField')(max_length=120, null=True, blank=True)),
            ('telefono_casa', self.gf('django.db.models.fields.PositiveIntegerField')(max_length=20)),
            ('telefono_celular', self.gf('django.db.models.fields.PositiveIntegerField')(max_length=20)),
            ('grado_instruccion', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('ocupacion', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True)),
            ('correo_electronico', self.gf('django.db.models.fields.EmailField')(max_length=75)),
        ))
        db.send_create_signal(u'voluntarios', ['Voluntario'])


    def backwards(self, orm):
        # Deleting model 'Voluntario'
        db.delete_table(u'voluntarios_voluntario')


    models = {
        u'voluntarios.voluntario': {
            'CI': ('django.db.models.fields.CharField', [], {'max_length': '10', 'primary_key': 'True'}),
            'Meta': {'object_name': 'Voluntario'},
            'apellido': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'correo_electronico': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'direccion': ('django.db.models.fields.CharField', [], {'max_length': '120', 'null': 'True', 'blank': 'True'}),
            'edad': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'estado_civil': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'fecha_nacimiento': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'genero': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'grado_instruccion': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'lugar_nacimiento': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'ocupacion': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'primer_nombre': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'telefono_casa': ('django.db.models.fields.PositiveIntegerField', [], {'max_length': '20'}),
            'telefono_celular': ('django.db.models.fields.PositiveIntegerField', [], {'max_length': '20'})
        }
    }

    complete_apps = ['voluntarios']