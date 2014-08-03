# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Proyecto'
        db.create_table(u'proyectos_proyecto', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'proyectos', ['Proyecto'])


    def backwards(self, orm):
        # Deleting model 'Proyecto'
        db.delete_table(u'proyectos_proyecto')


    models = {
        u'proyectos.proyecto': {
            'Meta': {'object_name': 'Proyecto'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['proyectos']