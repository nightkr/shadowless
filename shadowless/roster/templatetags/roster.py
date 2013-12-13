from django import template

register = template.Library()

def class_name_css_fix(value):
	return value.lower().replace(' ', '-')

register.filter('class_name_css_fix', class_name_css_fix)