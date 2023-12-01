from django import template

register = template.Library()

@register.filter(name='getattr')
def get_attribute(obj, attr):
    try:
        return getattr(obj, attr)
    except AttributeError:
        return None