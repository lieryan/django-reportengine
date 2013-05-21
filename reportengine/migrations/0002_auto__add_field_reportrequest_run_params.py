# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'ReportRequest.run_params'
        db.add_column('reportengine_reportrequest', 'run_params',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'ReportRequest.run_params'
        db.delete_column('reportengine_reportrequest', 'run_params')


    models = {
        'reportengine.reportrequest': {
            'Meta': {'object_name': 'ReportRequest'},
            'aggregates': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'completion_timestamp': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'namespace': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'params': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'request_made': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'db_index': 'True'}),
            'run_params': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'task': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'token': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_index': 'True'}),
            'viewed_on': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'})
        },
        'reportengine.reportrequestexport': {
            'Meta': {'object_name': 'ReportRequestExport'},
            'completion_timestamp': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'format': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'payload': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'report_request': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'exports'", 'to': "orm['reportengine.ReportRequest']"}),
            'request_made': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'db_index': 'True'}),
            'task': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'token': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_index': 'True'})
        },
        'reportengine.reportrequestrow': {
            'Meta': {'object_name': 'ReportRequestRow'},
            'data': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'report_request': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'rows'", 'to': "orm['reportengine.ReportRequest']"}),
            'row_number': ('django.db.models.fields.PositiveIntegerField', [], {})
        }
    }

    complete_apps = ['reportengine']