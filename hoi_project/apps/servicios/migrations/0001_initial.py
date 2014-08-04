# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Servicio'
        db.create_table(u'servicios_servicio', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('servicio', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('turno', self.gf('django.db.models.fields.CharField')(max_length=2)),
        ))
        db.send_create_signal(u'servicios', ['Servicio'])


    def backwards(self, orm):
        # Deleting model 'Servicio'
        db.delete_table(u'servicios_servicio')


    models = {
        u'servicios.servicio': {
            'Meta': {'object_name': 'Servicio'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'servicio': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'turno': ('django.db.models.fields.CharField', [], {'max_length': '2'})
        }
    }

    complete_apps = ['servicios']