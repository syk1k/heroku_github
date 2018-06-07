from django import template
from django.utils.html import conditional_escape
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter(needs_autoescape=True)
def initial_letter_filter(text, autoescape=None):
    first, other = text[0], text[1:]
    if autoescape:
        esc = conditional_escape
    else:
        esc = lambda x: x
    result = '<strong>%s</strong>%s' % (esc(first), esc(other))
    return mark_safe(result)



@register.simple_tag(name="mytag")
def my_tag(value):
    return value + 1


@register.inclusion_tag('template_tag.html', takes_context=True, name="tagg")
def my_inclusion_tag(context):
    val = context['message']
    return {"value":val}


@register.assignment_tag(name="ass_tag")
def the_tag(value):
    return value