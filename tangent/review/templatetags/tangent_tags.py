from django import template

register = template.Library()

@register.simple_tag
def b_day(email):
    return email
