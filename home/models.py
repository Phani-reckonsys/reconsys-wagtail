from django.db import models
from wagtail.models import Page, Orderable
from modelcluster.fields import ParentalKey
from wagtail.admin.panels import TabbedInterface, ObjectList, FieldPanel, InlinePanel

class NavItem(models.Model):
    name = models.CharField(max_length = 255, blank=True, help_text = "Navigation Link Name")



class HomePage(Page):
    # navbar content variables
    service_nav = models.CharField(max_length = 255, blank=True, help_text = "Services Navigation Link")
    ourworks_nav = models.CharField(max_length = 255, blank=True, help_text = "OurWorks Navigation Link")
    # services section content
    home_service_title = models.CharField(max_length = 255, blank=True, help_text = "Services Navigation Link")
    home_service_subtitle = models.CharField(max_length = 255, blank=True, help_text = "Services Navigation Link")
    home_service_content = models.CharField(max_length = 255, blank=True, help_text = "Services Navigation Link")
    # process section content
    home_process_title = models.CharField(max_length = 255, blank=True, help_text = "Services Navigation Link")
    home_process_subtitle = models.CharField(max_length = 255, blank=True, help_text = "Services Navigation Link")
    home_process_content = models.CharField(max_length = 255, blank=True, help_text = "Services Navigation Link")
    # HomePage images
    image = models.ForeignKey('wagtailimages.Image', null=True, blank = True, on_delete = models.SET_NULL, related_name = "+")
    casestudies_saascard_image = models.ForeignKey('wagtailimages.Image', null = True, blank = True, on_delete = models.SET_NULL, related_name = "+")
    casestudies_seniorcentriccard_image = models.ForeignKey('wagtailimages.Image', null = True, blank = True, on_delete = models.SET_NULL, related_name = "+")
    enquirebot_cofounder_image = models.ForeignKey('wagtailimages.Image', null = True, blank = True, on_delete = models.SET_NULL, related_name = "+")
    blogs_crmemail = models.ForeignKey('wagtailimages.Image', null = True, blank = True, on_delete = models.SET_NULL, related_name = "+")
    blogs_solvingcrmemail = models.ForeignKey('wagtailimages.Image', null = True, blank = True, on_delete = models.SET_NULL, related_name = "+")
    blogs_clutchreview = models.ForeignKey('wagtailimages.Image', null = True, blank = True, on_delete = models.SET_NULL, related_name = "+")
    # Adding field panels
    navbar_panels = [FieldPanel('service_nav'),FieldPanel('ourworks_nav')]
    content_panels = [FieldPanel('home_service_title'),FieldPanel('home_service_subtitle'), FieldPanel('home_service_content'), FieldPanel('home_process_title'),FieldPanel('home_process_subtitle'), FieldPanel('home_process_content')]
    image_panels = [FieldPanel('image'), FieldPanel('enquirebot_cofounder_image'), FieldPanel('casestudies_saascard_image'), FieldPanel('casestudies_seniorcentriccard_image'), FieldPanel('blogs_crmemail'), FieldPanel('blogs_solvingcrmemail'), FieldPanel('blogs_clutchreview')]
    service_card_panels = [InlinePanel('service_cards', label='label')]
    process_card_panels = [InlinePanel('process_cards', label='label')]
    edit_handler = TabbedInterface([
        ObjectList(navbar_panels, heading='navbar'),
        ObjectList(image_panels, heading= 'images'),
        ObjectList(content_panels, heading='Content'),
        ObjectList(service_card_panels, heading='ServiceCards'),
        ObjectList(process_card_panels, heading='ProcessCards'),
        ObjectList(Page.promote_panels, heading='Promote'),
    ])
    @property
    def cardservice(self):
        return self.service_cards.all()
    
    @property
    def cardprocess(self):
        return self.process_cards.all()


class HomeServiceCard(Orderable):
    card_icon = models.ForeignKey('wagtailimages.Image', null=True, blank = True, on_delete = models.SET_NULL, related_name = "+")
    title = models.CharField(max_length = 255, blank=True, help_text = "Services Navigation Link")
    description = models.CharField(max_length = 255, blank=True, help_text = "Services Navigation Link")

    page = ParentalKey(HomePage, on_delete = models.CASCADE, related_name = "service_cards")
    panels = [FieldPanel('card_icon'),FieldPanel('title'), FieldPanel('description')]

class HomeProcessCard(Orderable):
    pointer_icon = models.ForeignKey('wagtailimages.Image', null=True, blank = True, on_delete = models.SET_NULL, related_name = "+")
    line_svg = models.ForeignKey('wagtailimages.Image', null=True, blank = True, on_delete = models.SET_NULL, related_name = "+")
    dotted_mesh = models.ForeignKey('wagtailimages.Image', null=True, blank = True, on_delete = models.SET_NULL, related_name = "+")
    title = models.CharField(max_length = 255, blank=True, help_text = "Services Navigation Link")
    point1 = models.CharField(max_length = 255, blank=True, help_text = "Services Navigation Link")
    point2 = models.CharField(max_length = 255, blank=True, help_text = "Services Navigation Link")
    point3 = models.CharField(max_length = 255, blank=True, help_text = "Services Navigation Link")
    point4 = models.CharField(max_length = 255, blank=True, help_text = "Services Navigation Link")

    page = ParentalKey(HomePage, on_delete = models.CASCADE, related_name = "process_cards")
    panels = [FieldPanel('pointer_icon'),FieldPanel('point1'), FieldPanel('point2'), FieldPanel('point3'), FieldPanel('point4'), FieldPanel('title'), FieldPanel('dotted_mesh')]
