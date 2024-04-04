from django.db import models
from wagtail.models import Page, Orderable, ClusterableModel
from modelcluster.fields import ParentalKey
from modelcluster.fields import ForeignKey
from wagtail.admin.panels import TabbedInterface, ObjectList, FieldPanel, InlinePanel, TitleFieldPanel
# Create your models here.
class ServicesPage(Page):
    banner_panels = [InlinePanel('banner_row', label = 'label')]
    edit_handler = TabbedInterface([
        ObjectList(banner_panels, heading='Banner'),
    ])
    @property
    def rowbanner(self):
        return self.banner_row.all()

class bannerrow(Orderable):
    banner_image = models.ForeignKey('wagtailimages.Image', null=True, blank = True, on_delete = models.SET_NULL, related_name = "+")
    banner_text = models.CharField(max_length = 255, blank=True, help_text = "Services Navigation Link")

    page = ParentalKey(ServicesPage, on_delete = models.CASCADE, related_name = "banner_row")
    panels = [FieldPanel('banner_image'), FieldPanel('banner_text')]