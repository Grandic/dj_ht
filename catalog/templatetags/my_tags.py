from django import template

register = template.Library()


@register.filter(name='mediapath')
def mediapath(value):
    if value:
        return f'/media/{value}'
    return '#'


@register.simple_tag
def mediapath(val):
    if val:
        return f'/media/{val}'
    return '#'
