from django import template
from components.models import Navbar
register = template.Library()
# ...
# Advert snippets
@register.inclusion_tag('components/navbar.html', takes_context=True)
def navbar(context):
    return {
        'navbar': Navbar.objects.first(),
        'request': context['request'],
    }