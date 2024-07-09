from django import template
from components.models import Navbar, Contact, Footer, NavbarGreen, NavbarGrey, Welcomebackmodel, Servicesmegamenu

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
        'path': context.request.path,
    }

@register.inclusion_tag('snippets/navbargreen.html', takes_context=True)
def navbargreen(context):
    navbargreen  = NavbarGreen.objects.first()
    return {
        'navbargreen': navbargreen,
        'navitemsgreen': navbargreen.navitemsgreen.all(),
        'request': context['request'],
        'path': context.request.path,
    }

@register.inclusion_tag('snippets/navbargrey.html', takes_context=True)
def navbargrey(context):
    navbargrey  = NavbarGrey.objects.first()
    return {
        'navbargrey': navbargrey,
        'navitemsgrey': navbargrey.navitemsgrey.all(),
        'request': context['request'],
        'path': context.request.path,
    }

@register.inclusion_tag('snippets/contact.html', takes_context=True)
def contact(context):
    contact = Contact.objects.first()
    return {
        'contact': Contact.objects.first(),
        'servicesoptions': contact.servicesoptions.all(),
        'request': context['request'],
        'path': context.request.path,
    }

@register.inclusion_tag('snippets/footer.html', takes_context=True)
def footer(context):
    footer = Footer.objects.first()
    return {
        'footer': Footer.objects.first(),
        'footerimages': footer.footerimages.all(),
        'footeritems': footer.footeritems.all(),
        'socialitems': footer.socialitems.all(),
        'request': context['request'],
        'path': context.request.path,
    }

@register.inclusion_tag('snippets/welcomebackmodel.html', takes_context=True)
def welcomebackmodel(context):
    welcomebackmodel = Welcomebackmodel.objects.first()
    return{
        'welcomebackmodel': Welcomebackmodel.objects.first(),
        'request': context['request'],
    }


@register.inclusion_tag('snippets/servicesmegamenu.html', takes_context=True)
def servicesmegamenu(context):
    servicesmegamenu = Servicesmegamenu.objects.first()
    return{
        'servicesmegamenu': Servicesmegamenu.objects.first(),
        'servicesmenuitems': servicesmegamenu.servicesmenuitems.all(),
        'request': context['request'],
        'path': context.request.path,
    }
