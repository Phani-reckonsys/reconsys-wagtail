from django.db import models
from wagtail.admin.panels import FieldPanel, PageChooserPanel, InlinePanel
from wagtail.snippets.models import register_snippet
from wagtail.models import Orderable, ParentalKey, ClusterableModel

@register_snippet
class Navbar(ClusterableModel):
    # navbar content variables
    panels = [InlinePanel('navitems', heading='navbar')]

class NavItem(Orderable, models.Model):
    name = models.CharField(max_length = 255, blank=True, help_text = "Services Navigation Link")
    link = models.ForeignKey("wagtailcore.Page", null = True, blank = True, on_delete = models.SET_NULL, related_name = "+")

    navbar = ParentalKey(Navbar, on_delete = models.CASCADE, related_name="navitems")
    panels = [FieldPanel("name"), PageChooserPanel("link")
]

@register_snippet
class Footer(models.Model):
   pass

@register_snippet
class Contact(models.Model):
   pass

  
