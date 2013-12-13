from django.db import models
from django.conf import settings

from shadowless.fixdata import models as fixdata

class Guild(models.Model):
    unique_together = ("name", "realm")

    name = models.CharField(max_length=30)
    realm = models.ForeignKey(fixdata.Realm)

    @classmethod
    def main_guild(cls):
        return cls.objects.get_or_create(name=settings.WOW_MAIN_GUILD, realm=fixdata.Realm.objects.get(name=settings.WOW_MAIN_SERVER))[0]

    def __unicode__(self):
        return u'%s@%s' % (self.name, self.realm)

class GuildRank(models.Model):
    unique_together = (
        ("guild", "name"),
        ("guild", "armory_rank"),
    )

    name = models.CharField(max_length=30)
    guild = models.ForeignKey(Guild, related_name="ranks")
    armory_rank = models.IntegerField()

    def __unicode__(self):
        return u"%s - %s" % (self.guild, self.name)

class ClassSpec(models.Model):
    unique_together = ("name", "klass")

    name = models.CharField(max_length=30)
    klass = models.ForeignKey(fixdata.Class)
    role = models.ForeignKey(fixdata.Role)

    def __unicode__(self):
        return u"%s - %s (%s)" % (self.klass, self.name, self.role)

class Character(models.Model):
    unique_together = ("name", "realm")

    name = models.CharField(max_length=30)
    level = models.IntegerField()
    realm = models.ForeignKey(fixdata.Realm)
    race = models.ForeignKey(fixdata.Race)
    klass = models.ForeignKey(fixdata.Class, verbose_name="Class")
    rank = models.ForeignKey(GuildRank, related_name='members', null=True, verbose_name="Guild/Rank")
    specs = models.ManyToManyField(ClassSpec, related_name='+')

    def __unicode__(self):
        return u'%s@%s' % (self.name, self.realm)
