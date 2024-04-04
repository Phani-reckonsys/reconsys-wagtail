from django.db import models
from wagtail.models import Page, Orderable, ClusterableModel
from modelcluster.fields import ParentalKey
from modelcluster.fields import ForeignKey
from wagtail.admin.panels import TabbedInterface, ObjectList, FieldPanel, InlinePanel, TitleFieldPanel
# Create your models here.
class ServicesPage(Page):
    banner_title = models.CharField(max_length = 255, blank=True, help_text = "Banner section title")
    servicesoffered_title = models.CharField(max_length = 255, blank = True, help_text = "Services offered title")
    servicesoffered_content = models.CharField(max_length = 255, blank = True, help_text = "Services offered content")
    businesshelped_title = models.CharField(max_length = 255, blank = True, help_text = "Business helped title")
    businesshelped_subtitle = models.CharField(max_length = 255, blank = True, help_text = "Business helped subtitle")
    banner_panels = [FieldPanel('banner_title'), InlinePanel('banner_row', label = 'label')]
    servicesoffered_panels = [FieldPanel('servicesoffered_title'),FieldPanel('servicesoffered_content'), InlinePanel('services_offered', label = 'label')]
    businesshelped_panels = [FieldPanel('businesshelped_title'), FieldPanel('businesshelped_subtitle'), InlinePanel('business_helped_card')]
    edit_handler = TabbedInterface([
        ObjectList(banner_panels, heading='Banner'),
        ObjectList(servicesoffered_panels, heading='Services Offered'),
        ObjectList(businesshelped_panels, heading='Business Helped')
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