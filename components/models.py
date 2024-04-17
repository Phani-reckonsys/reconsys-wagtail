from django.db import models
from wagtail.admin.panels import FieldPanel, PageChooserPanel, InlinePanel
from wagtail.snippets.models import register_snippet
from wagtail.models import Orderable, ParentalKey, ClusterableModel

@register_snippet
class Navbar(ClusterableModel):
    Home_page_link = models.ForeignKey("wagtailcore.Page", null = True, blank = True, on_delete = models.SET_NULL, related_name = "+")
    Contact_page = models.CharField(max_length = 255, blank=True, help_text = "contactus Link")
    Contact_page_link = models.ForeignKey("wagtailcore.Page", null = True, blank = True, on_delete = models.SET_NULL, related_name = "+")
    bgcolor = models.CharField(max_length = 255, blank=True, help_text = "contactus Link")

    # navbar content variables
    panels = [InlinePanel('navitems', heading='navbar'), FieldPanel("Contact_page"), FieldPanel("bgcolor"), PageChooserPanel("Contact_page_link"), PageChooserPanel("Home_page_link")]

class NavItem(Orderable, models.Model):
    name = models.CharField(max_length = 255, blank=True, help_text = "Navigation link")
    link = models.ForeignKey("wagtailcore.Page", null = True, blank = True, on_delete = models.SET_NULL, related_name = "+")

    navbar = ParentalKey(Navbar, on_delete = models.CASCADE, related_name="navitems")
    panels = [FieldPanel("name"), PageChooserPanel("link")]


@register_snippet
class Footer(ClusterableModel):

    # navbar content variables
    panels = [InlinePanel('socialitems', heading='socialitems'), InlinePanel('footeritems', heading='footeritems')]

class SocialItems(Orderable, models.Model):
    name = models.CharField(max_length = 255, blank=True, help_text = "Navigation link")
    url = models.URLField(null=True, blank=True)

    navbar = ParentalKey(Footer, on_delete = models.CASCADE, related_name="socialitems")
    panels = [FieldPanel("name"), FieldPanel("url")]

class FooterItems(Orderable, models.Model):
    name = models.CharField(max_length = 255, blank=True, help_text = "Navigation link")
    url = models.URLField(null=True, blank=True)

    navbar = ParentalKey(Footer, on_delete = models.CASCADE, related_name="footeritems")
    panels = [FieldPanel("name"), FieldPanel("url")]


@register_snippet
class Contact(models.Model):
   pass

@register_snippet
class NavbarGreen(ClusterableModel):
    Home_page_link = models.ForeignKey("wagtailcore.Page", null = True, blank = True, on_delete = models.SET_NULL, related_name = "+")
    Contact_page = models.CharField(max_length = 255, blank=True, help_text = "contactus Link")
    Contact_page_link = models.ForeignKey("wagtailcore.Page", null = True, blank = True, on_delete = models.SET_NULL, related_name = "+")
    bgcolor = models.CharField(max_length = 255, blank=True, help_text = "contactus Link")

    # navbar content variables
    panels = [InlinePanel('navitemsgreen', heading='navbargreen'), FieldPanel("Contact_page"), FieldPanel("bgcolor"), PageChooserPanel("Contact_page_link"), PageChooserPanel("Home_page_link")]

class NavItemGreen(Orderable, models.Model):
    name = models.CharField(max_length = 255, blank=True, help_text = "Navigation link")
    link = models.ForeignKey("wagtailcore.Page", null = True, blank = True, on_delete = models.SET_NULL, related_name = "+")

    navbar = ParentalKey(NavbarGreen, on_delete = models.CASCADE, related_name="navitemsgreen")
    panels = [FieldPanel("name"), PageChooserPanel("link")] 

@register_snippet
class NavbarGrey(ClusterableModel):
    Home_page_link = models.ForeignKey("wagtailcore.Page", null = True, blank = True, on_delete = models.SET_NULL, related_name = "+")
    Contact_page = models.CharField(max_length = 255, blank=True, help_text = "contactus Link")
    Contact_page_link = models.ForeignKey("wagtailcore.Page", null = True, blank = True, on_delete = models.SET_NULL, related_name = "+")
    bgcolor = models.CharField(max_length = 255, blank=True, help_text = "contactus Link")

    # navbar content variables
    panels = [InlinePanel('navitemsgrey', heading='navbargrey'), FieldPanel("Contact_page"), FieldPanel("bgcolor"), PageChooserPanel("Contact_page_link"), PageChooserPanel("Home_page_link")]

class NavItemGrey(Orderable, models.Model):
    name = models.CharField(max_length = 255, blank=True, help_text = "Navigation link")
    link = models.ForeignKey("wagtailcore.Page", null = True, blank = True, on_delete = models.SET_NULL, related_name = "+")

    navbar = ParentalKey(NavbarGrey, on_delete = models.CASCADE, related_name="navitemsgrey")
    panels = [FieldPanel("name"), PageChooserPanel("link")] 
