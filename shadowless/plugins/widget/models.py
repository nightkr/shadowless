from cms.models.pluginmodel import CMSPlugin
from django.db import models

class WidgetModel(CMSPlugin):
    title = models.CharField(max_length=255)
    hide_title = models.BooleanField(default=False)

    def __unicode__(self):
        return self.title
