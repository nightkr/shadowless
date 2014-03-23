from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from shadowless.plugins.widget.models import WidgetModel

class Widget(CMSPluginBase):
    model = WidgetModel
    render_template = "widget/widget.haml"
    allow_children = True

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context

plugin_pool.register_plugin(Widget)
