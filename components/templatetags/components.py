from django import template
from components.models import Navbar, Contact, Footer
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

@register.inclusion_tag('snippets/contact.html', takes_context=True)
def contact(context):
    return {
        'contact': Contact.objects.first(),
        'request': context['request'],
    }

@register.inclusion_tag('snippets/footer.html', takes_context=True)
def footer(context):
    footer = Footer.objects.first()
    return {
        'footer': Footer.objects.first(),
        'footeritems': footer.footeritems.all(),
        'socialitems': footer.socialitems.all(),
        'request': context['request'],
    }
