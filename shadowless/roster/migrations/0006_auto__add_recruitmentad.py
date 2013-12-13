# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'RecruitmentAd'
        db.create_table(u'roster_recruitmentad', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('klass', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['fixdata.Class'])),
            ('role', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['fixdata.Role'])),
        ))
        db.send_create_signal(u'roster', ['RecruitmentAd'])


    def backwards(self, orm):
        # Deleting model 'RecruitmentAd'
        db.delete_table(u'roster_recruitmentad')


    models = {
        u'fixdata.class': {
            'Meta': {'object_name': 'Class'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'fixdata.race': {
            'Meta': {'object_name': 'Race'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'fixdata.realm': {
            'Meta': {'object_name': 'Realm'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'fixdata.role': {
            'Meta': {'object_name': 'Role'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'roster.character': {
            'Meta': {'object_name': 'Character'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'klass': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['fixdata.Class']"}),
            'level': ('django.db.models.fields.IntegerField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'race': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['fixdata.Race']"}),
            'rank': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'members'", 'null': 'True', 'to': u"orm['roster.GuildRank']"}),
            'realm': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['fixdata.Realm']"}),
            'specs': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'+'", 'symmetrical': 'False', 'to': u"orm['roster.ClassSpec']"})
        },
        u'roster.classspec': {
            'Meta': {'object_name': 'ClassSpec'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'klass': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['fixdata.Class']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'role': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['fixdata.Role']"})
        },
        u'roster.guild': {
            'Meta': {'object_name': 'Guild'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'realm': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['fixdata.Realm']"})
        },
        u'roster.guildrank': {
            'Meta': {'object_name': 'GuildRank'},
            'armory_rank': ('django.db.models.fields.IntegerField', [], {}),
            'guild': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'ranks'", 'to': u"orm['roster.Guild']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        u'roster.recruitmentad': {
            'Meta': {'object_name': 'RecruitmentAd'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'klass': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['fixdata.Class']"}),
            'role': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['fixdata.Role']"})
        }
    }

    complete_apps = ['roster']