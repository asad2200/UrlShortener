from django import template

register = template.Library()

def addclass(value, token):
    value.field.widget.attrs['class'] = token
    return value

register.filter(addclass)