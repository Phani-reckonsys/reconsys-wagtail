from django import template
from components.models import Navbar, Herosection
register = template.Library()
# ...
# Advert snippets
@register.inclusion_tag('components/navbar.html', takes_context=True)
def navbar(context):
    return {
        'navbar': Navbar.objects.first(),
        'request': context['request'],
    }

@register.inclusion_tag('components/herosection.html', takes_context=True)
def herosection(context):
    print(dir(context))
    return {
        'titles': Herosection.objects.values_list('herosection_title', flat=True).all(),
        'subtitles': Herosection.objects.values_list('herosection_subtitle', flat=True).all(),
        'count': Herosection.objects.count(),
        'request': context['request'],
    }