from django.db import models
from wagtail.models import Page, Orderable, ClusterableModel,StreamField
from modelcluster.fields import ParentalKey
from wagtail.fields import RichTextField
from modelcluster.fields import ForeignKey
from datetime import datetime

from wagtail.admin.panels import TabbedInterface, ObjectList, FieldPanel, InlinePanel, TitleFieldPanel
from components.blocks import HeroSectionBlock
# Create your models here.
class ServicesPage(Page):
    body = StreamField(
        [('herosection', HeroSectionBlock())
         
        ], null = True)
    # banner section
    banner_sidetitle = models.CharField(max_length = 255, blank=True, help_text = "Banner section title")
    banner_title = RichTextField(max_length = 255, blank=True, help_text = "Banner section title")
    # Services Offered Section
    servicesoffered_sidetitle = models.CharField(max_length = 255, blank = True, help_text = "Services offered title")
    servicesoffered_title = models.CharField(max_length = 255, blank = True, help_text = "Services offered title")
    servicesoffered_content = RichTextField(max_length = 255, blank = True, help_text = "Services offered content")
    # Business Helped Section
    businesshelped_sidetitle = models.CharField(max_length = 255, blank = True, help_text = "Business helped title")
    businesshelped_title = models.CharField(max_length = 255, blank = True, help_text = "Business helped title")
    businesshelped_subtitle = RichTextField(max_length = 255, blank = True, help_text = "Business helped subtitle")
    # Engagment Section
    engagment_sidetitle = models.CharField(max_length = 255, blank = True, help_text = "Business helped subtitle")
    engagment_title = models.CharField(max_length = 255, blank = True, help_text = "Business helped subtitle")
    engagment_subtitle = RichTextField(max_length = 255, blank = True, help_text = "Business helped subtitle")
    # Data Section
    datasection_sidetitle = models.CharField(max_length = 255, blank = True, help_text = "Business helped subtitle")
    datasection_title = models.CharField(max_length = 255, blank = True, help_text = "Business helped subtitle")
    datasection_subtitle = RichTextField(max_length = 255, blank = True, help_text = "Business helped subtitle")
    # Testimonials section
    testimonial_content = models.CharField(max_length = 255, blank = True, help_text = "Business helped subtitle")
    testimonial_name = models.CharField(max_length = 255, blank = True, help_text = "Business helped subtitle")
    testimonial_designation = models.CharField(max_length = 255, blank = True, help_text = "Business helped subtitle")
    testimonial_avatar = models.ForeignKey('wagtailimages.Image', null=True, blank = True, on_delete = models.SET_NULL, related_name = "+")
    # FAQ
    faqsection_sidetitle = models.CharField(max_length = 255, blank = True, help_text = "Business helped subtitle")
    faqsection_toptitle = models.CharField(max_length = 255, blank = True, help_text = "Business helped subtitle")
    faqsection_title = RichTextField(max_length = 255, blank = True, help_text = "Business helped subtitle")
    # Panels
    content_panels = [TitleFieldPanel('title')]
    banner_panels = [FieldPanel('banner_sidetitle'), FieldPanel('banner_title'), InlinePanel('banner_row', label = 'label')]
    body_panels = [FieldPanel('body')]
    servicesoffered_panels = [FieldPanel('servicesoffered_sidetitle'), FieldPanel('servicesoffered_title'),FieldPanel('servicesoffered_content'), InlinePanel('services_offered', label = 'label')]
    businesshelped_panels = [FieldPanel('businesshelped_sidetitle'), FieldPanel('businesshelped_title'), FieldPanel('businesshelped_subtitle'), InlinePanel('business_helped_card')]
    engagmentmodel_panels = [FieldPanel('engagment_sidetitle'), FieldPanel('engagment_title'), FieldPanel('engagment_subtitle'), InlinePanel('engagment_card')]
    datasection_panels = [FieldPanel('datasection_sidetitle'), FieldPanel('datasection_title'), FieldPanel('datasection_subtitle'), InlinePanel('datasection_stat')]
    faqsection_panels = [FieldPanel('faqsection_sidetitle'), FieldPanel('faqsection_toptitle'), FieldPanel('faqsection_title'), InlinePanel('faqsection_faq')]
    testimonial_panels = [FieldPanel('testimonial_content'), FieldPanel('testimonial_name'), FieldPanel('testimonial_designation'), FieldPanel('testimonial_avatar')]
    edit_handler = TabbedInterface([
        ObjectList(content_panels, heading= 'Content'),
        ObjectList(banner_panels, heading='Banner'),
        ObjectList(body_panels, heading='Body'),
        ObjectList(servicesoffered_panels, heading='Services Offered'),
        ObjectList(businesshelped_panels, heading='Business Helped'),
        ObjectList(engagmentmodel_panels, heading='Engagment Model'),
        ObjectList(datasection_panels, heading='Data Section'),
        ObjectList(testimonial_panels, heading='Testimonial Section'),
        ObjectList(faqsection_panels, heading='FAQ Section'),
        ObjectList(Page.promote_panels, heading='Promote'),
    ])
    @property
    def rowbanner(self):
        return self.banner_row.all()
    
    @property
    def offeredservices(self):
        return self.services_offered.all()
    
    @property
    def cardbusinesshelped(self):
        return self.business_helped_card.all()
    
    @property
    def cardengagment(self):
        return self.engagment_card.all()
    
    @property
    def statdatasection(self):
        return self.datasection_stat.all()
    
    @property
    def faqfaqsection(self):
        return self.faqsection_faq.all()
    

class BannerRow(Orderable):
    banner_image = models.ForeignKey('wagtailimages.Image', null=True, blank = True, on_delete = models.SET_NULL, related_name = "+")
    banner_text = RichTextField(max_length = 450, blank=True, help_text = "Services Navigation Link")

    page = ParentalKey(ServicesPage, on_delete = models.CASCADE, related_name = "banner_row")
    panels = [FieldPanel('banner_image'), FieldPanel('banner_text')]

class ServicesOffered(Orderable):
    question = models.CharField(max_length = 255, blank=True, help_text = "Services Navigation Link")
    answer = models.CharField(max_length = 255, blank=True, help_text = "Services Navigation Link")
    service_icon = models.ForeignKey('wagtailimages.Image', null=True, blank = True, on_delete = models.SET_NULL, related_name = "+")
    plus_icon = models.ForeignKey('wagtailimages.Image', null=True, blank = True, on_delete = models.SET_NULL, related_name = "+")
    card_link = models.ForeignKey("wagtailcore.Page", null = True, blank = True, on_delete = models.SET_NULL, related_name = "+")


    page = ParentalKey(ServicesPage, on_delete=models.CASCADE, related_name = "services_offered")
    panels = [FieldPanel('card_link'), FieldPanel('question'), FieldPanel('answer'), FieldPanel('service_icon'), FieldPanel('plus_icon')]

class BusinessHelpedCard(ClusterableModel):
    title = models.CharField(max_length = 255, blank=True, help_text = "Services Navigation Link")
    pointer_icon = models.ForeignKey('wagtailimages.Image', null=True, blank = True, on_delete = models.SET_NULL, related_name = "+")
    point1 = models.CharField(max_length = 255, blank=True, help_text = "Services Navigation Link")
    point2 = models.CharField(max_length = 255, blank=True, help_text = "Services Navigation Link")
    point3 = models.CharField(max_length = 255, blank=True, help_text = "Services Navigation Link")
    point4 = models.CharField(max_length = 255, blank=True, help_text = "Services Navigation Link")
    point5 = models.CharField(max_length = 255, blank=True, help_text = "Services Navigation Link")
    footer_image_1 = models.ForeignKey('wagtailimages.Image', null=True, blank = True, on_delete = models.SET_NULL, related_name = "+")
    footer_image_2 = models.ForeignKey('wagtailimages.Image', null=True, blank = True, on_delete = models.SET_NULL, related_name = "+")

    page = ParentalKey(ServicesPage, on_delete=models.CASCADE, related_name = "business_helped_card")
    panels = [FieldPanel('title'), FieldPanel('pointer_icon'), FieldPanel('point1'), FieldPanel('point2'), FieldPanel('point3'), FieldPanel('point4'), FieldPanel('point5'), FieldPanel('footer_image_1'), FieldPanel('footer_image_2')]
    
    @property
    def cardpointbusinesshelped(self):
        return self.business_helped_card_point.all()


class BusinessHelpedCardPoint(Orderable):
    pointer_icon = models.ForeignKey('wagtailimages.Image', null=True, blank = True, on_delete = models.SET_NULL, related_name = "+")
    point = models.CharField(max_length = 255, blank=True, help_text = "Services Navigation Link")

    page = ParentalKey(BusinessHelpedCard, on_delete=models.CASCADE, related_name = "business_helped_card_point")
    panels = [FieldPanel('pointer_icon'), FieldPanel('point')]

class EngagmentCard(Orderable):
    cover_image = models.ForeignKey('wagtailimages.Image', null=True, blank = True, on_delete = models.SET_NULL, related_name = "+")
    title = models.CharField(max_length = 255, blank=True, help_text = "Services Navigation Link")
    subtitle = models.CharField(max_length = 255, blank=True, help_text = "Services Navigation Link")

    page = ParentalKey(ServicesPage, on_delete=models.CASCADE, related_name = "engagment_card")
    panels = [FieldPanel('cover_image'), FieldPanel('title'), FieldPanel('subtitle')]

class DatasectionStat(Orderable):
    data = models.CharField(max_length = 255, blank=True, help_text = "data")
    title = models.CharField(max_length = 255, blank=True, help_text = "title")

    page = ParentalKey(ServicesPage, on_delete=models.CASCADE, related_name = "datasection_stat")
    panels = [FieldPanel('data'), FieldPanel('title')]

class faqsectionfaq(Orderable):
    question = models.CharField(max_length = 255, blank=True, help_text = "data")
    answer = models.CharField(max_length = 255, blank=True, help_text = "title")

    page = ParentalKey(ServicesPage, on_delete=models.CASCADE, related_name = "faqsection_faq")
    panels = [FieldPanel('question'), FieldPanel('answer')]