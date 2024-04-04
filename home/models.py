from django.db import models
from wagtail.models import Page, Orderable, ClusterableModel
from modelcluster.fields import ParentalKey
from modelcluster.fields import ForeignKey
from wagtail.admin.panels import TabbedInterface, ObjectList, FieldPanel, InlinePanel, TitleFieldPanel


class HomePage(Page):
    # services section content
    home_service_title = models.CharField(max_length = 255, blank=True, help_text = "Services Navigation Link")
    home_service_subtitle = models.CharField(max_length = 255, blank=True, help_text = "Services Navigation Link")
    home_service_content = models.CharField(max_length = 255, blank=True, help_text = "Services Navigation Link")
    # process section content
    home_process_title = models.CharField(max_length = 255, blank=True, help_text = "Services Navigation Link")
    home_process_subtitle = models.CharField(max_length = 255, blank=True, help_text = "Services Navigation Link")
    home_process_content = models.CharField(max_length = 255, blank=True, help_text = "Services Navigation Link")
    home_process_technology_title = models.CharField(max_length = 255, blank=True, help_text = "Services Navigation Link")
    home_process_technology_content = models.CharField(max_length = 255, blank=True, help_text = "Services Navigation Link")
    # Rating Section Content
    home_rating_title = models.CharField(max_length = 255, blank=True, help_text = "Services Navigation Link")
    home_rating_subtitle = models.CharField(max_length = 255, blank=True, help_text = "Services Navigation Link")
    home_rating_testimonial_title = models.CharField(max_length = 255, blank=True, help_text = "Services Navigation Link")
    home_rating_testimonial_content = models.CharField(max_length = 255, blank=True, help_text = "Services Navigation Link")
    home_rating_testimonial_name = models.CharField(max_length = 255, blank=True, help_text = "Services Navigation Link")
    home_rating_testimonial_designation = models.CharField(max_length = 255, blank=True, help_text = "Services Navigation Link")
    #industries section content
    home_industries_title = models.CharField(max_length = 255, blank=True, help_text = "Services Navigation Link")
    home_industries_subtitle = models.CharField(max_length = 255, blank=True, help_text = "Services Navigation Link")
    home_industries_content = models.CharField(max_length = 255, blank=True, help_text = "Services Navigation Link")
    # HomePage images
    image = models.ForeignKey('wagtailimages.Image', null=True, blank = True, on_delete = models.SET_NULL, related_name = "+")
    casestudies_saascard_image = models.ForeignKey('wagtailimages.Image', null = True, blank = True, on_delete = models.SET_NULL, related_name = "+")
    great_place_to_work_badge = models.ForeignKey('wagtailimages.Image', null = True, blank = True, on_delete = models.SET_NULL, related_name = "+")
    casestudies_seniorcentriccard_image = models.ForeignKey('wagtailimages.Image', null = True, blank = True, on_delete = models.SET_NULL, related_name = "+")
    enquirebot_cofounder_image = models.ForeignKey('wagtailimages.Image', null = True, blank = True, on_delete = models.SET_NULL, related_name = "+")
    blogs_crmemail = models.ForeignKey('wagtailimages.Image', null = True, blank = True, on_delete = models.SET_NULL, related_name = "+")
    blogs_solvingcrmemail = models.ForeignKey('wagtailimages.Image', null = True, blank = True, on_delete = models.SET_NULL, related_name = "+")
    blogs_clutchreview = models.ForeignKey('wagtailimages.Image', null = True, blank = True, on_delete = models.SET_NULL, related_name = "+")
    # Adding field panels
    
    content_panels = [TitleFieldPanel('title'),FieldPanel('home_service_title'),FieldPanel('home_service_subtitle'), FieldPanel('home_service_content'), FieldPanel('home_process_title'),FieldPanel('home_process_subtitle'), FieldPanel('home_process_content'), FieldPanel('home_process_technology_title'), FieldPanel('home_process_technology_content'), FieldPanel('home_rating_title'), FieldPanel('home_rating_subtitle'), FieldPanel('home_rating_testimonial_title'), FieldPanel('home_rating_testimonial_content'), FieldPanel('home_rating_testimonial_name'), FieldPanel('home_rating_testimonial_designation')]
    image_panels = [FieldPanel('image'), FieldPanel('enquirebot_cofounder_image'), FieldPanel('casestudies_saascard_image'), FieldPanel('casestudies_seniorcentriccard_image'), FieldPanel('blogs_crmemail'), FieldPanel('blogs_solvingcrmemail'), FieldPanel('blogs_clutchreview'), FieldPanel('great_place_to_work_badge')]
    service_card_panels = [InlinePanel('service_cards', label='label')]
    process_card_panels = [InlinePanel('process_cards', label='label')]
    industries_section_panel = [FieldPanel('home_industries_title'), FieldPanel('home_industries_subtitle'), FieldPanel('home_industries_content'), InlinePanel('industries_cards', label='label') ]
    edit_handler = TabbedInterface([
        ObjectList(image_panels, heading= 'images'),
        ObjectList(content_panels, heading='Content'),
        ObjectList(service_card_panels, heading='ServiceCards'),
        ObjectList(process_card_panels, heading='ProcessCards'),
        ObjectList(industries_section_panel, heading='IndustriesSection'),
        ObjectList(Page.promote_panels, heading='Promote'),
    ])
    @property
    def cardservice(self):
        return self.service_cards.all()
    
    @property
    def cardprocess(self):
        return self.process_cards.all()
    
    @property
    def cardindustries(self):
        return self.industries_cards.all()

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

class IndustriesSectionCard(ClusterableModel):
    card_icon = models.ForeignKey('wagtailimages.Image', null=True, blank = True, on_delete = models.SET_NULL, related_name = "+")
    footer_testimonial1 = models.ForeignKey('wagtailimages.Image', null=True, blank = True, on_delete = models.SET_NULL, related_name = "+")
    footer_testimonial2 = models.ForeignKey('wagtailimages.Image', null=True, blank = True, on_delete = models.SET_NULL, related_name = "+")
    card_title = models.CharField(max_length= 255, blank = True, help_text= "card title")

    page = ParentalKey(HomePage, on_delete = models.CASCADE, related_name = "industries_cards")
    panels = [FieldPanel('card_icon'), FieldPanel('card_title'), FieldPanel('footer_testimonial1'), FieldPanel('footer_testimonial2'), InlinePanel('industries_cards_point', label= 'label')]

    @property
    def cardindustriespoint(self):
        return self.industries_cards_point.all()

class IndusrtrialSectionCardPoint(Orderable):
    pointer_icon = models.ForeignKey('wagtailimages.Image', null = True, blank = True, on_delete= models.SET_NULL, related_name = "+")
    point = models.CharField(max_length= 255, blank = True, help_text= "card title")

    indusrtrial_section_card = ParentalKey(IndustriesSectionCard, on_delete = models.CASCADE, related_name = "industries_cards_point")
    panels = [FieldPanel('pointer_icon'), FieldPanel('point')]




