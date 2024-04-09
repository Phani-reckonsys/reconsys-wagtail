from django import template
from components.models import Navbar, Herosection, Footer
register = template.Library()
# ...
# Advert snippets
@register.inclusion_tag('snippets/navbar.html', takes_context=True)
def navbar(context):
    navbar  = Navbar.objects.first()
    return {
        'navbar': navbar,
        'navitems': navbar.navitems.all(),
        'request': context['request'],
    }

@register.inclusion_tag('snippets/footer.html', takes_context=True)
def footer(context):
    return {
        'footer': Footer.objects.first(),
        'request': context['request'],
    }
