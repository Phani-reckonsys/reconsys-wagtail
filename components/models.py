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
    ourworks_page_link = models.ForeignKey("wagtailcore.Page", null = True, blank = True, on_delete = models.SET_NULL, related_name = "+")
    
    panels = [InlinePanel('servicesitems', heading='servicesitems'), InlinePanel('socialitems', heading='socialitems'), InlinePanel('footeritems', heading='footeritems'), InlinePanel('footerimages', heading='footerimages'), FieldPanel("ourworks_page_link")]
   
    
class FooterImages(Orderable,models.Model):
    image = models.ForeignKey('wagtailimages.Image', null=True, blank = True, on_delete = models.SET_NULL, related_name = "+")

    footer = ParentalKey(Footer, on_delete = models.CASCADE, related_name="footerimages")
    panels = [FieldPanel("image")]


class SocialItems(Orderable, models.Model):
    name = models.CharField(max_length = 255, blank=True, help_text = "Navigation link")
    url = models.URLField(null=True, blank=True)

    navbar = ParentalKey(Footer, on_delete = models.CASCADE, related_name="socialitems")
    panels = [FieldPanel("name"), FieldPanel("url")]

class FooterItems(Orderable, models.Model):
    name = models.CharField(max_length = 255, blank=True, help_text = "Navigation link")
    url = models.ForeignKey("wagtailcore.Page", null = True, blank = True, on_delete = models.SET_NULL, related_name = "+")

    navbar = ParentalKey(Footer, on_delete = models.CASCADE, related_name="footeritems")
    panels = [FieldPanel("name"), PageChooserPanel("url")]

class ServicesItems(Orderable, models.Model):
    name = models.CharField(max_length = 255, blank=True, help_text = "Navigation link")
    url = models.ForeignKey("wagtailcore.Page", null = True, blank = True, on_delete = models.SET_NULL, related_name = "+")

    navbar = ParentalKey(Footer, on_delete = models.CASCADE, related_name="servicesitems")
    panels = [FieldPanel("name"), PageChooserPanel("url")]




@register_snippet
class Contact(ClusterableModel):
   ourworks_page_link = models.ForeignKey("wagtailcore.Page", null = True, blank = True, on_delete = models.SET_NULL, related_name = "+")
   panels = [InlinePanel('servicesoptions', heading="ServicesOptions"), InlinePanel('reviewcards'), FieldPanel('ourworks_page_link')]

class SevicesOptions(Orderable,models.Model):
    service = models.CharField(max_length = 255, blank=True, help_text = "Services Offred")

    contact = ParentalKey(Contact, on_delete = models.CASCADE, related_name="servicesoptions")
    panels = [FieldPanel("service")]

class ReviewCards(Orderable, models.Model):
    cardlink = models.URLField( null = True, blank = True)
    rating =models.CharField(max_length = 255, blank=True, help_text = "contactus Link")
    text =models.CharField(max_length = 255, blank=True, help_text = "contactus Link")
    image = models.ForeignKey('wagtailimages.Image', null=True, blank = True, on_delete = models.SET_NULL, related_name = "+")

    reviewcards = ParentalKey(Contact, on_delete = models.CASCADE, related_name="reviewcards")
    panels = [FieldPanel("rating"), FieldPanel("text"), FieldPanel("image"), FieldPanel("cardlink")]



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

@register_snippet
class Servicesmegamenu(ClusterableModel):    
    service_page_text = models.CharField(max_length = 255, blank=True, help_text = "contactus Link")
    service_page_link = models.ForeignKey("wagtailcore.page", null = True, blank = True, on_delete = models.SET_NULL, related_name = "+")
    image = models.ForeignKey('wagtailimages.Image', null=True, blank = True, on_delete = models.SET_NULL, related_name = "+")

    panels = [InlinePanel('servicesmenuitems', heading="servicesmegaitems"), FieldPanel("service_page_text"), FieldPanel("service_page_link"), FieldPanel("image")]

class ServicesMenuItems(Orderable, models.Model):
    name = models.CharField(max_length = 255, blank=True, help_text="Navigation Link")
    link = models.ForeignKey("wagtailcore.Page", null=True, help_text = "page link", on_delete = models.SET_NULL)

    megamenu = ParentalKey(Servicesmegamenu, on_delete=models.CASCADE, related_name="servicesmenuitems")
    panels = [FieldPanel("name"), PageChooserPanel("link")]

@register_snippet
class Badgessnippet(ClusterableModel):
    title = models.CharField(max_length = 255, blank=True, help_text = "contactus Link")

    panels = [InlinePanel('badges', heading="badges"), FieldPanel("title")]

class Badges(Orderable, models.Model):
    image = models.ForeignKey('wagtailimages.Image', null=True, blank = True, on_delete = models.SET_NULL, related_name = "+")

    badges = ParentalKey(Badgessnippet, on_delete=models.CASCADE, related_name="badges")
    panels = [FieldPanel("image")]

@register_snippet
class Welcomebackmodel(ClusterableModel):
    headline = models.CharField(max_length = 255, blank=True, help_text = "Navigation link")
    content = models.CharField(max_length = 255, blank=True, help_text = "Navigation link")
    btn_text= models.CharField(max_length = 255, blank=True, help_text = "Navigation link")
    sideimage = models.ForeignKey('wagtailimages.Image', null=True, blank = True, on_delete = models.SET_NULL, related_name = "+")
    contactus_page_link = models.ForeignKey("wagtailcore.Page", null = True, blank = True, on_delete = models.SET_NULL, related_name = "+")


    panels = [ FieldPanel("headline"), FieldPanel("content"), FieldPanel("btn_text"), PageChooserPanel("sideimage"), PageChooserPanel("contactus_page_link")]


@register_snippet
class Technologymegamenu(ClusterableModel):    
    technology_page_text = models.CharField(max_length = 255, blank=True, help_text = "contactus Link")
    technology_page_link = models.ForeignKey("wagtailcore.page", null = True, blank = True, on_delete = models.SET_NULL, related_name = "+")
    image = models.ForeignKey('wagtailimages.Image', null=True, blank = True, on_delete = models.SET_NULL, related_name = "+")

    panels = [InlinePanel('technologymenuitems', heading="technologymegaitems"), FieldPanel("technology_page_text"), FieldPanel("technology_page_link"), FieldPanel("image")]

class TechnologyMenuItems(Orderable, models.Model):
    name = models.CharField(max_length = 255, blank=True, help_text="Navigation Link")
    link = models.ForeignKey("wagtailcore.Page", null=True, help_text = "page link", on_delete = models.SET_NULL)

    megamenu = ParentalKey(Technologymegamenu, on_delete=models.CASCADE, related_name="technologymenuitems")
    panels = [FieldPanel("name"), PageChooserPanel("link")]
