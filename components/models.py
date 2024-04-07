from django.db import models
from wagtail.admin.panels import FieldPanel
from wagtail.snippets.models import register_snippet

@register_snippet
class Navbar(models.Model):
    # navbar content variables
    service_nav = models.CharField(max_length = 255, blank=True, help_text = "Services Navigation Link")
    ourworks_nav = models.CharField(max_length = 255, blank=True, help_text = "OurWorks Navigation Link")
    panels = [FieldPanel('service_nav'),FieldPanel('ourworks_nav')]


@register_snippet
class Herosection(models.Model):
    panels = []


    
