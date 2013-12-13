from django.db import models

class Class(models.Model):
    name = models.CharField(max_length=30, unique=True)

    def __unicode__(self):
        return self.name

class Race(models.Model):
    name = models.CharField(max_length=30, unique=True)

    def __unicode__(self):
        return self.name

class Realm(models.Model):
    name = models.CharField(max_length=30, unique=True)

    def __unicode__(self):
        return self.name

class Role(models.Model):
	name = models.CharField(max_length=30, unique=True)

	def __unicode__(self):
		return self.name
