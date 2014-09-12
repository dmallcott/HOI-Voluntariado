# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Servicios.fecha'
        db.add_column(u'registros_servicios', 'fecha',
                      self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2014, 9, 11, 0, 0)),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Servicios.fecha'
        db.delete_column(u'registros_servicios', 'fecha')


    models = {
        u'registros.proyectos': {
            'Meta': {'object_name': 'Proyectos'},
            'fecha': ('django.db.models.fields.DateField', [], {}),
            'horas': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'proyecto': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['voluntariado.Proyecto']"}),
            'voluntario': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['voluntariado.Voluntario']"})
        },
        u'registros.servicios': {
            'Meta': {'object_name': 'Servicios'},
            'fecha': ('django.db.models.fields.DateField', [], {}),
            'horas': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'servicio': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['voluntariado.Servicio']"}),
            'voluntario': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['voluntariado.Voluntario']"})
        },
        u'voluntariado.organizacion': {
            'Meta': {'object_name': 'Organizacion'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'})
        },
        u'voluntariado.proyecto': {
            'Meta': {'object_name': 'Proyecto'},
            'dependencia': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'especialidad': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'estatus': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        u'voluntariado.servicio': {
            'Meta': {'object_name': 'Servicio'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'servicio': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'turno': ('django.db.models.fields.CharField', [], {'max_length': '2'})
        },
        u'voluntariado.voluntario': {
            'CI': ('django.db.models.fields.CharField', [], {'max_length': '10', 'primary_key': 'True'}),
            'Meta': {'object_name': 'Voluntario'},
            'apellido': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'correo_electronico': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'direccion': ('django.db.models.fields.CharField', [], {'max_length': '120', 'blank': 'True'}),
            'estado_civil': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'fecha_nacimiento': ('django.db.models.fields.DateField', [], {'blank': 'True'}),
            'genero': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'grado_instruccion': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'institucion': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['voluntariado.Organizacion']", 'blank': 'True'}),
            'lugar_nacimiento': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'ocupacion': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'primer_nombre': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'telefono_casa': ('django.db.models.fields.PositiveIntegerField', [], {'max_length': '20'}),
            'telefono_celular': ('django.db.models.fields.PositiveIntegerField', [], {'max_length': '20'})
        }
    }

    complete_apps = ['registros']