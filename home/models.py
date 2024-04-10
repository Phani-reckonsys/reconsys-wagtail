from django.db import models
from wagtail.models import Page, Orderable, ClusterableModel, StreamField
from modelcluster.fields import ParentalKey
from modelcluster.fields import ForeignKey
from wagtail.admin.panels import TabbedInterface, ObjectList, FieldPanel, InlinePanel, TitleFieldPanel, MultiFieldPanel
from components.blocks import HeroSectionBlock, OurMissionBlock, OurVisionBlock, OurValuesBlock

class HomePage(Page):
    herosection = StreamField(
        [('herosecion', HeroSectionBlock())
         
        ], null = True)
    # services section content
    home_service_title = models.CharField(max_length = 255, blank=True, help_text = "Services Navigation Link")
    home_service_subtitle = models.CharField(max_length = 255, blank=True, help_text = "Services Navigation Link")
    home_service_content = models.CharField(max_length = 255, blank=True, help_text = "Services Navigation Link")
    home_service_button_text = models.CharField(max_length= 255, blank = True, help_text= "card title")
    home_service_button_icon = models.ForeignKey('wagtailimages.Image', null = True, blank = True, on_delete= models.SET_NULL, related_name = "+")
    # process section content
    home_process_title = models.CharField(max_length = 255, blank=True, help_text = "Services Navigation Link")
    home_process_subtitle = models.CharField(max_length = 255, blank=True, help_text = "Services Navigation Link")
    home_process_technology_title = models.CharField(max_length = 255, blank=True, help_text = "Services Navigation Link")
    home_process_technology_content = models.CharField(max_length = 255, blank=True, help_text = "Services Navigation Link")
    dotted_mesh = models.ForeignKey('wagtailimages.Image', null=True, blank = True, on_delete = models.SET_NULL, related_name = "+")
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
    # Why Reckonsys
    home_whyreckonsys_title = models.CharField(max_length = 255, blank=True, help_text = "Services Navigation Link")
    home_whyreckonsys_subtitle = models.CharField(max_length = 255, blank=True, help_text = "Services Navigation Link")
    home_whyreckonsys_content = models.CharField(max_length = 255, blank=True, help_text = "Services Navigation Link")
    # Case Studies
    home_casestudies_title = models.CharField(max_length = 255, blank=True, help_text = "Services Navigation Link")
    home_casestudies_subtitle = models.CharField(max_length = 255, blank=True, help_text = "Services Navigation Link")
     # Testimonial
    home_testimonials_title = models.CharField(max_length = 255, blank=True, help_text = "Services Navigation Link")
    home_testimonials_subtitle = models.CharField(max_length = 255, blank=True, help_text = "Services Navigation Link")

    # images
    image = models.ForeignKey('wagtailimages.Image', null=True, blank = True, on_delete = models.SET_NULL, related_name = "+")
    casestudies_saascard_image = models.ForeignKey('wagtailimages.Image', null = True, blank = True, on_delete = models.SET_NULL, related_name = "+")
    great_place_to_work_badge = models.ForeignKey('wagtailimages.Image', null = True, blank = True, on_delete = models.SET_NULL, related_name = "+")
    casestudies_seniorcentriccard_image = models.ForeignKey('wagtailimages.Image', null = True, blank = True, on_delete = models.SET_NULL, related_name = "+")
    enquirebot_cofounder_image = models.ForeignKey('wagtailimages.Image', null = True, blank = True, on_delete = models.SET_NULL, related_name = "+")
    blogs_crmemail = models.ForeignKey('wagtailimages.Image', null = True, blank = True, on_delete = models.SET_NULL, related_name = "+")
    blogs_solvingcrmemail = models.ForeignKey('wagtailimages.Image', null = True, blank = True, on_delete = models.SET_NULL, related_name = "+")
    blogs_clutchreview = models.ForeignKey('wagtailimages.Image', null = True, blank = True, on_delete = models.SET_NULL, related_name = "+")
    # Adding field panels
    
    content_panels = [TitleFieldPanel('title')]
    herosection_panels = [FieldPanel('herosection')]
    image_panels = [FieldPanel('image'), FieldPanel('enquirebot_cofounder_image'), FieldPanel('casestudies_saascard_image'), FieldPanel('casestudies_seniorcentriccard_image'), FieldPanel('blogs_crmemail'), FieldPanel('blogs_solvingcrmemail'), FieldPanel('blogs_clutchreview'), FieldPanel('great_place_to_work_badge')]
    services_offered_panels = [FieldPanel('home_service_title'),FieldPanel('home_service_subtitle'), FieldPanel('home_service_content'),MultiFieldPanel(heading = "Service Button", children=(FieldPanel('home_service_button_text'), FieldPanel('home_service_button_icon') )), InlinePanel('service_cards', label='Service Card')]
    process_followed_panels = [FieldPanel('home_process_title'),FieldPanel('home_process_subtitle'), FieldPanel('home_process_technology_title'), FieldPanel('home_process_technology_content'), FieldPanel('dotted_mesh'), InlinePanel('process_cards', label='label'), InlinePanel('technologies_stack', label='Technologies Stack')]
    rating_panels =  [FieldPanel('home_rating_title'), FieldPanel('home_rating_subtitle'), FieldPanel('home_rating_testimonial_title'), FieldPanel('home_rating_testimonial_content'), FieldPanel('home_rating_testimonial_name'), FieldPanel('home_rating_testimonial_designation')]
    industries_section_panel = [FieldPanel('home_industries_title'), FieldPanel('home_industries_subtitle'), FieldPanel('home_industries_content'), InlinePanel('industries_cards', label='card') ]
    whyreckonsys_section_panel = [FieldPanel('home_whyreckonsys_title'), FieldPanel('home_whyreckonsys_subtitle'), FieldPanel('home_whyreckonsys_content'), InlinePanel('whyreckonsys_cards', label='card') ]
    casestudies_panel = [FieldPanel('home_casestudies_title'), FieldPanel('home_casestudies_subtitle'), InlinePanel('casestudies_cards', label='case studies card') ]  
    testimonial_panel = [FieldPanel('home_testimonials_title'), FieldPanel('home_testimonials_subtitle'), InlinePanel('testimonial_cards', label='testimonial card') ]  
    edit_handler = TabbedInterface([
        ObjectList(content_panels, heading= 'Content'),
        ObjectList(image_panels, heading= 'Images'),
        ObjectList(herosection_panels, heading= 'Herosection'),
        ObjectList(services_offered_panels, heading='Service  Offered'),
        ObjectList(process_followed_panels, heading='Process Followed'),
        ObjectList(industries_section_panel, heading='IndustriesSection'),
        ObjectList(rating_panels, heading='Rating'),
        ObjectList(whyreckonsys_section_panel, heading='Why Reckonsys'),
        ObjectList(casestudies_panel, heading='case studies'),
        ObjectList(testimonial_panel, heading='Testimonial'),
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
    
    @property
    def stacktechnologies(self):
        return self.technologies_stack.all()

    @property
    def cardswhyreckonsys(self):
        return self.whyreckonsys_cards.all()
    
    @property
    def cardscasestudy(self):
        return self.casestudies_cards.all()
    
    @property
    def cardstestimonial(self):
        return self.testimonial_cards.all()

class HomeServiceCard(Orderable):
    card_icon = models.ForeignKey('wagtailimages.Image', null=True, blank = True, on_delete = models.SET_NULL, related_name = "+")
    title = models.CharField(max_length = 255, blank=True, help_text = "Services Navigation Link")
    description = models.CharField(max_length = 255, blank=True, help_text = "Services Navigation Link")

    page = ParentalKey(HomePage, on_delete = models.CASCADE, related_name = "service_cards")
    panels = [FieldPanel('card_icon'),FieldPanel('title'), FieldPanel('description')]

class HomeProcessCard(Orderable):
    pointer_icon = models.ForeignKey('wagtailimages.Image', null=True, blank = True, on_delete = models.SET_NULL, related_name = "+")
    line_svg = models.ForeignKey('wagtailimages.Image', null=True, blank = True, on_delete = models.SET_NULL, related_name = "+")
    title = models.CharField(max_length = 255, blank=True, help_text = "Services Navigation Link")
    point1 = models.CharField(max_length = 255, blank=True, help_text = "Services Navigation Link")
    point2 = models.CharField(max_length = 255, blank=True, help_text = "Services Navigation Link")
    point3 = models.CharField(max_length = 255, blank=True, help_text = "Services Navigation Link")
    point4 = models.CharField(max_length = 255, blank=True, help_text = "Services Navigation Link")

    page = ParentalKey(HomePage, on_delete = models.CASCADE, related_name = "process_cards")
    panels = [FieldPanel('pointer_icon'),FieldPanel('point1'), FieldPanel('point2'), FieldPanel('point3'), FieldPanel('point4'), FieldPanel('title')]

class TechnologiesStack(ClusterableModel):
    title = models.CharField(max_length = 255, blank = True, help_text = "Technology Stack Group Name")

    page = ParentalKey(HomePage, on_delete = models.CASCADE, related_name = "technologies_stack")
    panels = [FieldPanel('title'), InlinePanel('technologies',  label="Techologies")]

    @property
    def technology(self):
        return self.technologies.all()

class technologies(Orderable):
    icon = models.ForeignKey('wagtailimages.Image', null = True, blank = True, on_delete= models.SET_NULL, related_name = "+")

    page = ParentalKey(TechnologiesStack, on_delete = models.CASCADE, related_name = "technologies")
    panels = [FieldPanel('icon')]



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

class HomeWhyReckonsyCard(Orderable):
    image= models.ForeignKey('wagtailimages.Image', null=True, blank = True, on_delete = models.SET_NULL, related_name = "+")
    description = models.CharField(max_length = 255, blank=True, help_text = "Services Navigation Link")

    page = ParentalKey(HomePage, on_delete = models.CASCADE, related_name = "whyreckonsys_cards")
    panels = [FieldPanel('image'), FieldPanel('description')]


class HomeCaseStudiesCard(Orderable):
    cover_image = models.ForeignKey('wagtailimages.Image', null=True, blank = True, on_delete = models.SET_NULL, related_name = "+")
    title = models.CharField(max_length = 255, blank=True, help_text = "Services Navigation Link")
    subtitle = models.CharField(max_length = 255, blank=True, help_text = "Services Navigation Link")
    data1 = models.CharField(max_length = 255, blank=True, help_text = "Services Navigation Link")
    data2 = models.CharField(max_length = 255, blank=True, help_text = "Services Navigation Link")
    label1 = models.CharField(max_length = 255, blank=True, help_text = "Services Navigation Link")
    label2 = models.CharField(max_length = 255, blank=True, help_text = "Services Navigation Link")

    page = ParentalKey(HomePage, on_delete = models.CASCADE, related_name = "casestudies_cards")
    panels = [FieldPanel('cover_image'),FieldPanel('title'), FieldPanel('subtitle'), FieldPanel('data1'), FieldPanel('data2'), FieldPanel('label1'), FieldPanel('label2')]

class HomeTestimonialCard(Orderable):
    name = models.CharField(max_length = 255, blank=True, help_text = "Services Navigation Link")
    designation = models.CharField(max_length = 255, blank=True, help_text = "Services Navigation Link")
    content = models.CharField(max_length = 255, blank=True, help_text = "Services Navigation Link")

    page = ParentalKey(HomePage, on_delete = models.CASCADE, related_name = "testimonial_cards")
    panels = [FieldPanel('name'), FieldPanel('designation'), FieldPanel('content')]



class AboutusPage(Page):
    body = StreamField(
        [('herosecion', HeroSectionBlock()),
         ('ourmission', OurMissionBlock()),
         ('ourvision', OurVisionBlock()),
         ('ourvalues', OurValuesBlock()),
         
        ], null = True)
    
    body_panels = [FieldPanel('body')]

    edit_handler = TabbedInterface([
        ObjectList(Page.content_panels, heading= 'Content'),
        ObjectList(body_panels, heading= 'Body'),
        ObjectList(Page.promote_panels, heading='Promote'),
    ])
