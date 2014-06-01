# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Voluntario'
        db.create_table(u'voluntarios_voluntario', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('primer_nombre', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal(u'voluntarios', ['Voluntario'])


    def backwards(self, orm):
        # Deleting model 'Voluntario'
        db.delete_table(u'voluntarios_voluntario')


    models = {
        u'voluntarios.voluntario': {
            'Meta': {'object_name': 'Voluntario'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'primer_nombre': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['voluntarios']