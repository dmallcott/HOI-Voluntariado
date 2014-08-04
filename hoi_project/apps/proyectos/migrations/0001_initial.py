# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Proyecto'
        db.create_table(u'proyectos_proyecto', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('titulo', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('institucion', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('especialidad', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('dependencia', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('estatus', self.gf('django.db.models.fields.CharField')(max_length=1)),
        ))
        db.send_create_signal(u'proyectos', ['Proyecto'])

        # Adding model 'Proyecto_Voluntario'
        db.create_table(u'proyectos_proyecto_voluntario', (
            ('proyecto', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['proyectos.Proyecto'], unique=True, primary_key=True)),
            ('voluntario', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['voluntarios.Voluntario'])),
            ('horas', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
        ))
        db.send_create_signal(u'proyectos', ['Proyecto_Voluntario'])


    def backwards(self, orm):
        # Deleting model 'Proyecto'
        db.delete_table(u'proyectos_proyecto')

        # Deleting model 'Proyecto_Voluntario'
        db.delete_table(u'proyectos_proyecto_voluntario')


    models = {
        u'proyectos.proyecto': {
            'Meta': {'object_name': 'Proyecto'},
            'dependencia': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'especialidad': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'estatus': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'institucion': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        u'proyectos.proyecto_voluntario': {
            'Meta': {'object_name': 'Proyecto_Voluntario'},
            'horas': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'proyecto': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['proyectos.Proyecto']", 'unique': 'True', 'primary_key': 'True'}),
            'voluntario': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['voluntarios.Voluntario']"})
        },
        u'voluntarios.voluntario': {
            'CI': ('django.db.models.fields.CharField', [], {'max_length': '10', 'primary_key': 'True'}),
            'Meta': {'object_name': 'Voluntario'},
            'apellido': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'correo_electronico': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'direccion': ('django.db.models.fields.CharField', [], {'max_length': '120', 'blank': 'True'}),
            'edad': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'estado_civil': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'fecha_nacimiento': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'genero': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'grado_instruccion': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'lugar_nacimiento': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'ocupacion': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'primer_nombre': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'telefono_casa': ('django.db.models.fields.PositiveIntegerField', [], {'max_length': '20'}),
            'telefono_celular': ('django.db.models.fields.PositiveIntegerField', [], {'max_length': '20'})
        }
    }

    complete_apps = ['proyectos']