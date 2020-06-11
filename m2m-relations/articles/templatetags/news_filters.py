from django import template

register = template.Library()


@register.filter
def key(dict_in: dict, key_name):
    return dict_in.get(key_name)







