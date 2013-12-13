# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):
    depends_on = (
        ("fixdata", "0001_initial"),
    )

    def forwards(self, orm):
        # Adding model 'Guild'
        db.create_table(u'roster_guild', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('realm', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['fixdata.Realm'])),
        ))
        db.send_create_signal(u'roster', ['Guild'])

        # Adding model 'GuildRank'
        db.create_table(u'roster_guildrank', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('guild', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['roster.Guild'])),
            ('armory_rank', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'roster', ['GuildRank'])

        # Adding model 'Character'
        db.create_table(u'roster_character', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('realm', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['fixdata.Realm'])),
            ('race', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['fixdata.Race'])),
            ('klass', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['fixdata.Class'])),
            ('rank', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['roster.GuildRank'])),
        ))
        db.send_create_signal(u'roster', ['Character'])


    def backwards(self, orm):
        # Deleting model 'Guild'
        db.delete_table(u'roster_guild')

        # Deleting model 'GuildRank'
        db.delete_table(u'roster_guildrank')

        # Deleting model 'Character'
        db.delete_table(u'roster_character')


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
        u'roster.character': {
            'Meta': {'object_name': 'Character'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'klass': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['fixdata.Class']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'race': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['fixdata.Race']"}),
            'rank': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['roster.GuildRank']"}),
            'realm': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['fixdata.Realm']"})
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
            'guild': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['roster.Guild']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['roster']