# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ReportRequest'
        db.create_table('reportengine_reportrequest', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('request_made', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, db_index=True)),
            ('completion_timestamp', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('token', self.gf('django.db.models.fields.CharField')(max_length=255, db_index=True)),
            ('task', self.gf('django.db.models.fields.CharField')(max_length=128, blank=True)),
            ('namespace', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('slug', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('params', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('viewed_on', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('aggregates', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('reportengine', ['ReportRequest'])

        # Adding model 'ReportRequestRow'
        db.create_table('reportengine_reportrequestrow', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('report_request', self.gf('django.db.models.fields.related.ForeignKey')(related_name='rows', to=orm['reportengine.ReportRequest'])),
            ('row_number', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('data', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('reportengine', ['ReportRequestRow'])

        # Adding model 'ReportRequestExport'
        db.create_table('reportengine_reportrequestexport', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('request_made', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, db_index=True)),
            ('completion_timestamp', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('token', self.gf('django.db.models.fields.CharField')(max_length=255, db_index=True)),
            ('task', self.gf('django.db.models.fields.CharField')(max_length=128, blank=True)),
            ('report_request', self.gf('django.db.models.fields.related.ForeignKey')(related_name='exports', to=orm['reportengine.ReportRequest'])),
            ('format', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('payload', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
        ))
        db.send_create_signal('reportengine', ['ReportRequestExport'])


    def backwards(self, orm):
        # Deleting model 'ReportRequest'
        db.delete_table('reportengine_reportrequest')

        # Deleting model 'ReportRequestRow'
        db.delete_table('reportengine_reportrequestrow')

        # Deleting model 'ReportRequestExport'
        db.delete_table('reportengine_reportrequestexport')


    models = {
        'reportengine.reportrequest': {
            'Meta': {'object_name': 'ReportRequest'},
            'aggregates': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'completion_timestamp': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'namespace': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'params': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'request_made': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'db_index': 'True'}),
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