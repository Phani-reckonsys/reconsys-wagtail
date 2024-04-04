from django.db import models
from wagtail.models import Page, Orderable, ClusterableModel
from modelcluster.fields import ParentalKey
from modelcluster.fields import ForeignKey
from wagtail.admin.panels import TabbedInterface, ObjectList, FieldPanel, InlinePanel, TitleFieldPanel
# Create your models here.
class ServicesPage(Page):
    # banner section
    banner_title = models.CharField(max_length = 255, blank=True, help_text = "Banner section title")
    # Services Offered Section
    servicesoffered_title = models.CharField(max_length = 255, blank = True, help_text = "Services offered title")
    servicesoffered_content = models.CharField(max_length = 255, blank = True, help_text = "Services offered content")
    # Business Helped Section
    businesshelped_title = models.CharField(max_length = 255, blank = True, help_text = "Business helped title")
    businesshelped_subtitle = models.CharField(max_length = 255, blank = True, help_text = "Business helped subtitle")
    # Engagment Section
    engagment_title = models.CharField(max_length = 255, blank = True, help_text = "Business helped subtitle")
    engagment_subtitle = models.CharField(max_length = 255, blank = True, help_text = "Business helped subtitle")
    # Data Section
    datasection_title = models.CharField(max_length = 255, blank = True, help_text = "Business helped subtitle")
    datasection_subtitle = models.CharField(max_length = 255, blank = True, help_text = "Business helped subtitle")
    # Testimonials section
    testimonial_content = models.CharField(max_length = 255, blank = True, help_text = "Business helped subtitle")
    testimonial_name = models.CharField(max_length = 255, blank = True, help_text = "Business helped subtitle")
    testimonial_designation = models.CharField(max_length = 255, blank = True, help_text = "Business helped subtitle")
    testimonial_avatar = models.ForeignKey('wagtailimages.Image', null=True, blank = True, on_delete = models.SET_NULL, related_name = "+")
    # FAQ
    faqsection_title_top = models.CharField(max_length = 255, blank = True, help_text = "Business helped subtitle")
    faqsection_title_bottom = models.CharField(max_length = 255, blank = True, help_text = "Business helped subtitle")
    # Panels
    banner_panels = [FieldPanel('banner_title'), InlinePanel('banner_row', label = 'label')]
    servicesoffered_panels = [FieldPanel('servicesoffered_title'),FieldPanel('servicesoffered_content'), InlinePanel('services_offered', label = 'label')]
    businesshelped_panels = [FieldPanel('businesshelped_title'), FieldPanel('businesshelped_subtitle'), InlinePanel('business_helped_card')]
    engagmentmodel_panels = [FieldPanel('engagment_title'), FieldPanel('engagment_subtitle'), InlinePanel('engagment_card')]
    datasection_panels = [FieldPanel('datasection_title'), FieldPanel('datasection_subtitle'), InlinePanel('datasection_stat')]
    faqsection_panels = [FieldPanel('faqsection_title_top'), FieldPanel('faqsection_title_bottom'), InlinePanel('faqsection_faq')]
    testimonial_panels = [FieldPanel('testimonial_content'), FieldPanel('testimonial_name'), FieldPanel('testimonial_designation'), FieldPanel('testimonial_avatar')]
    edit_handler = TabbedInterface([
        ObjectList(banner_panels, heading='Banner'),
        ObjectList(servicesoffered_panels, heading='Services Offered'),
        ObjectList(businesshelped_panels, heading='Business Helped'),
        ObjectList(engagmentmodel_panels, heading='Engagment Model'),
        ObjectList(datasection_panels, heading='Data Section'),
        ObjectList(testimonial_panels, heading='Testimonial Section'),
        ObjectList(faqsection_panels, heading='FAQ Section')
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
    banner_text = models.CharField(max_length = 255, blank=True, help_text = "Services Navigation Link")

    page = ParentalKey(ServicesPage, on_delete = models.CASCADE, related_name = "banner_row")
    panels = [FieldPanel('banner_image'), FieldPanel('banner_text')]

class ServicesOffered(Orderable):
    question = models.CharField(max_length = 255, blank=True, help_text = "Services Navigation Link")
    answer = models.CharField(max_length = 255, blank=True, help_text = "Services Navigation Link")
    service_icon = models.ForeignKey('wagtailimages.Image', null=True, blank = True, on_delete = models.SET_NULL, related_name = "+")
    plus_icon = models.ForeignKey('wagtailimages.Image', null=True, blank = True, on_delete = models.SET_NULL, related_name = "+")

    page = ParentalKey(ServicesPage, on_delete=models.CASCADE, related_name = "services_offered")
    panels = [FieldPanel('question'), FieldPanel('answer'), FieldPanel('service_icon'), FieldPanel('plus_icon')]

class BusinessHelpedCard(ClusterableModel):
    title = models.CharField(max_length = 255, blank=True, help_text = "Services Navigation Link")
    footer_image_1 = models.ForeignKey('wagtailimages.Image', null=True, blank = True, on_delete = models.SET_NULL, related_name = "+")
    footer_image_2 = models.ForeignKey('wagtailimages.Image', null=True, blank = True, on_delete = models.SET_NULL, related_name = "+")

    page = ParentalKey(ServicesPage, on_delete=models.CASCADE, related_name = "business_helped_card")
    panels = [FieldPanel('title'), InlinePanel('business_helped_card_point', label= 'label'), FieldPanel('footer_image_1'), FieldPanel('footer_image_2')]
    
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