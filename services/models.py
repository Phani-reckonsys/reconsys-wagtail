from django.db import models
from wagtail.models import Page, Orderable, ClusterableModel
from modelcluster.fields import ParentalKey
from modelcluster.fields import ForeignKey
from wagtail.admin.panels import TabbedInterface, ObjectList, FieldPanel, InlinePanel, TitleFieldPanel
# Create your models here.
class ServicesPage(Page):
    pass