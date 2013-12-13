from cms.api import CMSPluginBase, CMSPlugin, plugin_pool
from shadowless.plugins.widget.models import WidgetModel
#from cms.plugin_pool import plugin_pool

class Widget(CMSPluginBase):
    model = WidgetModel
    render_template = "widget/widget.haml"
    allow_children = True

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context

plugin_pool.register_plugin(Widget)
