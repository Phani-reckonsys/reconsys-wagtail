from django.db import models
from wagtail.models import Page, Orderable, ClusterableModel, StreamField
from wagtail.fields import RichTextField
from wagtail.blocks import StreamBlock
from modelcluster.fields import ParentalKey
from modelcluster.fields import ForeignKey
from wagtail.admin.panels import TabbedInterface, ObjectList, FieldPanel, InlinePanel, TitleFieldPanel, MultiFieldPanel
from components.blocks import HeroSectionBlock, OurMissionBlock, OurVisionBlock, OurValuesBlock, OurJourneyBlock, OurGalleryBlock, OurTestimonialBlock, BlogsHerosection, BlogsWrapperBlock, CoverImageBlock, CultureBlock, OneColScrollerSection, BenifitsBlock, OurWorksHerosectionBlock, OurWorksDisplayBlock, HomeTestimonialsBlock, HomeBlogsBlock, ContactUsTestimonialBlock, ContactModelBlock, OutlineGreyButtonBlock, PrivacyPolicyBlock, TestimonialGenericBlock, BadgesBlock, RatingBlock, ThankyouBlock, BlogHeaderBlock, BlogBodyBlock, ServicesHeroSectionBlock

class HomePage(Page):
    herosection = StreamField(
        [('herosecion', HeroSectionBlock())

         
        ], null = True)
    # services section content
    home_service_sidetitle = models.CharField(max_length = 255, blank=True, help_text = "Services Side Title")
    home_service_title = models.CharField(max_length = 255, blank=True, help_text = "Services Title")
    home_service_subtitle = RichTextField(max_length = 255, blank=True, help_text = "Services Subtitle")
    home_service_content = models.CharField(max_length = 255, blank=True, help_text = "Services Content")
    outline_grey_button = StreamField([('button', OutlineGreyButtonBlock())], null = True)

    # process section content
    home_process_sidetitle = models.CharField(max_length = 255, blank=True, help_text = "Services Navigation Link")
    home_process_title = models.CharField(max_length = 255, blank=True, help_text = "Services Navigation Link")
    home_process_subtitle = RichTextField(max_length = 255, blank=True, help_text = "Services Navigation Link")
    home_process_technology_title = models.CharField(max_length = 255, blank=True, help_text = "Services Navigation Link")
    home_process_technology_content = models.CharField(max_length = 255, blank=True, help_text = "Services Navigation Link")
    dotted_mesh = models.ForeignKey('wagtailimages.Image', null=True, blank = True, on_delete = models.SET_NULL, related_name = "+")
    #industries section content
    home_industries_sidetitle = models.CharField(max_length = 255, blank=True, help_text = "Services Navigation Link")
    home_industries_title = models.CharField(max_length = 255, blank=True, help_text = "Services Navigation Link")
    home_industries_subtitle = RichTextField(max_length = 255, blank=True, help_text = "Services Navigation Link")
    home_industries_content = models.CharField(max_length = 255, blank=True, help_text = "Services Navigation Link")

    # Why Reckonsys
    home_whyreckonsys_sidetitle = models.CharField(max_length = 255, blank=True, help_text = "Services Navigation Link")
    home_whyreckonsys_title = models.CharField(max_length = 255, blank=True, help_text = "Services Navigation Link")
    home_whyreckonsys_subtitle = RichTextField(max_length = 255, blank=True, help_text = "Services Navigation Link")
    home_whyreckonsys_content = models.CharField(max_length = 255, blank=True, help_text = "Services Navigation Link")
    # Case Studies
    home_casestudies_sidetitle = models.CharField(max_length = 255, blank=True, help_text = "Services Navigation Link")
    home_casestudies_title = models.CharField(max_length = 255, blank=True, help_text = "Services Navigation Link")
    home_casestudies_subtitle = RichTextField(max_length = 255, blank=True, help_text = "Services Navigation Link")

    body = StreamField([
        ("hometesimonials", HomeTestimonialsBlock()),
        ("homeblogs", HomeBlogsBlock()),
        ("badges", BadgesBlock()),
        ("Rating", RatingBlock()),
        # ('contactmodel', ContactModelBlock())
        ], null=True)
    # Adding field panels
    
    content_panels = [TitleFieldPanel('title')]
    herosection_panels = [FieldPanel('herosection')]
    services_offered_panels = [FieldPanel('home_service_sidetitle'), FieldPanel('home_service_title'),FieldPanel('home_service_subtitle'), FieldPanel('home_service_content'), FieldPanel('outline_grey_button'),  InlinePanel('service_cards', label='Service Card')]
    process_followed_panels = [FieldPanel('home_process_sidetitle'), FieldPanel('home_process_title'), FieldPanel('home_process_subtitle'), FieldPanel('home_process_technology_title'), FieldPanel('home_process_technology_content'), FieldPanel('dotted_mesh'), InlinePanel('process_cards', label='label'), InlinePanel('technologies_stack', label='Technologies Stack')]
    industries_section_panel = [FieldPanel('home_industries_sidetitle'), FieldPanel('home_industries_title'), FieldPanel('home_industries_subtitle'), FieldPanel('home_industries_content'), InlinePanel('industries_cards', label='card') ]
    whyreckonsys_section_panel = [FieldPanel('home_whyreckonsys_sidetitle'), FieldPanel('home_whyreckonsys_title'), FieldPanel('home_whyreckonsys_subtitle'), FieldPanel('home_whyreckonsys_content'), InlinePanel('whyreckonsys_cards', label='card') ]
    casestudies_panel = [FieldPanel('home_casestudies_sidetitle'), FieldPanel('home_casestudies_title'), FieldPanel('home_casestudies_subtitle'), InlinePanel('casestudies_cards', label='case studies card') ]  
    body_panel = [FieldPanel('body')]
    edit_handler = TabbedInterface([
        ObjectList(content_panels, heading= 'Content'),
        ObjectList(herosection_panels, heading= 'Herosection'),
        ObjectList(services_offered_panels, heading='Service  Offered'),
        ObjectList(process_followed_panels, heading='Process Followed'),
        ObjectList(industries_section_panel, heading='IndustriesSection'),
        ObjectList(whyreckonsys_section_panel, heading='Why Reckonsys'),
        ObjectList(casestudies_panel, heading='case studies'),
        ObjectList(body_panel, heading='Add New Sections'),
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
    final_pointer_icon = models.ForeignKey('wagtailimages.Image', null=True, blank = True, on_delete = models.SET_NULL, related_name = "+")
    title = models.CharField(max_length = 255, blank=True, help_text = "Services Navigation Link")
    point1 = models.CharField(max_length = 255, blank=True, help_text = "Services Navigation Link")
    point2 = models.CharField(max_length = 255, blank=True, help_text = "Services Navigation Link")
    point3 = models.CharField(max_length = 255, blank=True, help_text = "Services Navigation Link")
    point4 = models.CharField(max_length = 255, blank=True, help_text = "Services Navigation Link")

    page = ParentalKey(HomePage, on_delete = models.CASCADE, related_name = "process_cards")
    panels = [FieldPanel('pointer_icon'), FieldPanel('final_pointer_icon'), FieldPanel('point1'), FieldPanel('point2'), FieldPanel('point3'), FieldPanel('point4'), FieldPanel('title')]

class TechnologiesStack(ClusterableModel):
    title = models.CharField(max_length = 255, blank = True, help_text = "Technology Stack Group Name")

    page = ParentalKey(HomePage, on_delete = models.CASCADE, related_name = "technologies_stack")
    panels = [FieldPanel('title'), InlinePanel('technologies',  label="Techologies")]

    @property
    def technology(self):
        return self.technologies.all()

class technologies(Orderable):
    icon = models.ForeignKey('wagtailimages.Image', null = True, blank = True, on_delete= models.SET_NULL, related_name = "+")
    text = models.CharField(max_length = 255, blank = True, help_text = "Technology Stack Group Name")
    subtext = models.CharField(max_length = 255, blank = True, help_text = "Technology Stack Group Name")

    page = ParentalKey(TechnologiesStack, on_delete = models.CASCADE, related_name = "technologies")
    panels = [FieldPanel('icon'), FieldPanel('text'), FieldPanel('subtext')]



class IndustriesSectionCard(ClusterableModel):
    card_icon = models.ForeignKey('wagtailimages.Image', null=True, blank = True, on_delete = models.SET_NULL, related_name = "+")
    footer_testimonial1 = models.ForeignKey('wagtailimages.Image', null=True, blank = True, on_delete = models.SET_NULL, related_name = "+")
    footer_testimonial2 = models.ForeignKey('wagtailimages.Image', null=True, blank = True, on_delete = models.SET_NULL, related_name = "+")
    card_title = models.CharField(max_length= 255, blank = True, help_text= "card title")
    pointer_icon = models.ForeignKey('wagtailimages.Image', null = True, blank = True, on_delete= models.SET_NULL, related_name = "+")
    point1 = models.CharField(max_length = 255, blank=True, help_text = "Services Navigation Link")
    point2 = models.CharField(max_length = 255, blank=True, help_text = "Services Navigation Link")
    point3 = models.CharField(max_length = 255, blank=True, help_text = "Services Navigation Link")
    point4 = models.CharField(max_length = 255, blank=True, help_text = "Services Navigation Link")
    point5 = models.CharField(max_length = 255, blank=True, help_text = "Services Navigation Link")

    page = ParentalKey(HomePage, on_delete = models.CASCADE, related_name = "industries_cards")
    panels = [FieldPanel('card_icon'), FieldPanel('card_title'), FieldPanel('pointer_icon'), FieldPanel('point1'), FieldPanel('point2'),  FieldPanel('point3'), FieldPanel('point4'), FieldPanel('point5'), FieldPanel('footer_testimonial1'), FieldPanel('footer_testimonial2')]

    @property
    def cardindustriespoint(self):
        return self.industries_cards_point.all()

class IndusrtrialSectionCardPoint(Orderable):
    point = models.CharField(max_length= 255, blank = True, help_text= "card title")

    indusrtrial_section_card = ParentalKey(IndustriesSectionCard, on_delete = models.CASCADE, related_name = "industries_cards_point")
    panels = [ FieldPanel('point')]

class HomeWhyReckonsyCard(Orderable):
    image= models.ForeignKey('wagtailimages.Image', null=True, blank = True, on_delete = models.SET_NULL, related_name = "+")
    description = RichTextField(max_length = 255, blank=True, help_text = "Services Navigation Link")

    page = ParentalKey(HomePage, on_delete = models.CASCADE, related_name = "whyreckonsys_cards")
    panels = [FieldPanel('image'), FieldPanel('description')]


class HomeCaseStudiesCard(Orderable):
    bgcolor = models.CharField(max_length = 255, blank=True, help_text = "Services Navigation Link")
    cover_image = models.ForeignKey('wagtailimages.Image', null=True, blank = True, on_delete = models.SET_NULL, related_name = "+")
    title = models.CharField(max_length = 255, blank=True, help_text = "Services Navigation Link")
    subtitle = models.CharField(max_length = 255, blank=True, help_text = "Services Navigation Link")
    data1 = models.CharField(max_length = 255, blank=True, help_text = "Services Navigation Link")
    label1 = models.CharField(max_length = 255, blank=True, help_text = "Services Navigation Link")
    data2 = models.CharField(max_length = 255, blank=True, help_text = "Services Navigation Link")
    label2 = models.CharField(max_length = 255, blank=True, help_text = "Services Navigation Link")

    page = ParentalKey(HomePage, on_delete = models.CASCADE, related_name = "casestudies_cards")
    panels = [FieldPanel('cover_image'), FieldPanel('bgcolor') ,FieldPanel('title'), FieldPanel('subtitle'), FieldPanel('data1'), FieldPanel('label1'), FieldPanel('data2'), FieldPanel('label2')]

class HomeTestimonialCard(Orderable):
    name = models.CharField(max_length = 255, blank=True, help_text = "Services Navigation Link")
    designation = models.CharField(max_length = 255, blank=True, help_text = "Services Navigation Link")
    content = models.CharField(max_length = 255, blank=True, help_text = "Services Navigation Link")

    page = ParentalKey(HomePage, on_delete = models.CASCADE, related_name = "testimonial_cards")
    panels = [FieldPanel('name'), FieldPanel('designation'), FieldPanel('content')]



class AboutusPage(Page):
    body = StreamField(
        [('herosection', HeroSectionBlock()),
         ('ourmission', OurMissionBlock()),
         ('ourvision', OurVisionBlock()),
         ('ourvalues', OurValuesBlock()),
         ('ourjourney', OurJourneyBlock()),
         ('ourgallery', OurGalleryBlock()),
         ('ourtestimonial', OurTestimonialBlock()),
         
        ], null = True)
    
    body_panels = [FieldPanel('body')]

    edit_handler = TabbedInterface([
        ObjectList(Page.content_panels, heading= 'Content'),
        ObjectList(body_panels, heading= 'Body'),
        ObjectList(Page.promote_panels, heading='Promote'),
    ])


class BlogPage(Page):
    body = StreamField(
        [('herosection', HeroSectionBlock()),
         ('ourmission', OurMissionBlock()),
         ('ourvision', OurVisionBlock()),
         ('ourvalues', OurValuesBlock()),
         ('ourjourney', OurJourneyBlock()),
         ('ourgallery', OurGalleryBlock()),
         ('ourtestimonial', OurTestimonialBlock()),
         ('blogsherosection', BlogsHerosection()),
         ('blogswrapper', BlogsWrapperBlock()),

        ], null = True)
    
    body_panels = [FieldPanel('body')]

    edit_handler = TabbedInterface([
        ObjectList(Page.content_panels, heading= 'Content'),
        ObjectList(body_panels, heading= 'Body'),
        ObjectList(Page.promote_panels, heading='Promote'),
    ])

class CareerPage(Page):
    body = StreamField(
        [('herosection', HeroSectionBlock()),
         ('ourmission', OurMissionBlock()),
         ('ourvision', OurVisionBlock()),
         ('ourvalues', OurValuesBlock()),
         ('ourjourney', OurJourneyBlock()),
         ('ourgallery', OurGalleryBlock()),
         ('ourtestimonial', OurTestimonialBlock()),
         ('blogsherosection', BlogsHerosection()),
         ('coverImage', CoverImageBlock()),
         ('culture', CultureBlock()),
         ('onecolscrollersection', OneColScrollerSection()),
         ('BenifitsBlock', BenifitsBlock()),
         
        ], null = True)
    
    body_panels = [FieldPanel('body')]

    edit_handler = TabbedInterface([
        ObjectList(Page.content_panels, heading= 'Content'),
        ObjectList(body_panels, heading= 'Body'),
        ObjectList(Page.promote_panels, heading='Promote'),
    ])


class OurworksPage(Page):
    body = StreamField(
        [('herosection', HeroSectionBlock()),
         ('ourmission', OurMissionBlock()),
         ('ourvision', OurVisionBlock()),
         ('ourvalues', OurValuesBlock()),
         ('ourjourney', OurJourneyBlock()),
         ('ourgallery', OurGalleryBlock()),
         ('ourtestimonial', OurTestimonialBlock()),
         ('blogsherosection', BlogsHerosection()),
         ('coverImage', CoverImageBlock()),
         ('culture', CultureBlock()),
         ('onecolscrollersection', OneColScrollerSection()),
         ('BenifitsBlock', BenifitsBlock()),
         ('OurworksHerosection', OurWorksHerosectionBlock()),
         ('OurworksDisplay', OurWorksDisplayBlock()),
         ('TestimonialGeneric', TestimonialGenericBlock()),
         
        ], null = True)
    
    body_panels = [FieldPanel('body')]

    edit_handler = TabbedInterface([
        ObjectList(Page.content_panels, heading= 'Content'),
        ObjectList(body_panels, heading= 'Body'),
        ObjectList(Page.promote_panels, heading='Promote'),
    ])

class ContactusPage(Page):
    body = StreamField(
        [('herosection', HeroSectionBlock()),
         ('ourmission', OurMissionBlock()),
         ('ourvision', OurVisionBlock()),
         ('ourvalues', OurValuesBlock()),
         ('ourjourney', OurJourneyBlock()),
         ('ourgallery', OurGalleryBlock()),
         ('ourtestimonial', OurTestimonialBlock()),
         ('blogsherosection', BlogsHerosection()),
         ('coverImage', CoverImageBlock()),
         ('culture', CultureBlock()),
         ('onecolscrollersection', OneColScrollerSection()),
         ('BenifitsBlock', BenifitsBlock()),
         ('OurworksHerosection', OurWorksHerosectionBlock()),
         ('OurworksDisplay', OurWorksDisplayBlock()),
         ('ContactusTesimonial', ContactUsTestimonialBlock()),
         
        ], null = True)
    
    body_panels = [FieldPanel('body')]

    edit_handler = TabbedInterface([
        ObjectList(Page.content_panels, heading= 'Content'),
        ObjectList(body_panels, heading= 'Body'),
        ObjectList(Page.promote_panels, heading='Promote'),
    ])

class PersonalblogPage(Page):
    blogheader = StreamField([('blogheader', BlogHeaderBlock())], null = True)
    blogbody = StreamField([('blogbody', BlogBodyBlock())], null = True)
    
    blogheader_panels = [FieldPanel('blogheader')]
    blogbody_panels = [FieldPanel('blogbody')]

    edit_handler = TabbedInterface([
        ObjectList(Page.content_panels, heading= 'Content'),
        ObjectList(blogheader_panels, heading= 'BlogHeader'),
        ObjectList(blogbody_panels, heading= 'BlogBody'),
        ObjectList(Page.promote_panels, heading='Promote'),
    ])



class ThankyouPage(Page):
    body = StreamField(
        [('herosection', HeroSectionBlock()),
         ('ourmission', OurMissionBlock()),
         ('ourvision', OurVisionBlock()),
         ('ourvalues', OurValuesBlock()),
         ('ourjourney', OurJourneyBlock()),
         ('ourgallery', OurGalleryBlock()),
         ('ourtestimonial', OurTestimonialBlock()),
         ('blogsherosection', BlogsHerosection()),
         ('coverImage', CoverImageBlock()),
         ('culture', CultureBlock()),
         ('onecolscrollersection', OneColScrollerSection()),
         ('BenifitsBlock', BenifitsBlock()),
         ('OurworksHerosection', OurWorksHerosectionBlock()),
         ('OurworksDisplay', OurWorksDisplayBlock()),
         ('ContactusTesimonial', ContactUsTestimonialBlock()),
         ('thankyoublock', ThankyouBlock()),
         
        ], null = True)
    
    body_panels = [FieldPanel('body')]

    edit_handler = TabbedInterface([
        ObjectList(Page.content_panels, heading= 'Content'),
        ObjectList(body_panels, heading= 'Body'),
        ObjectList(Page.promote_panels, heading='Promote'),
    ])


class PrivacypolicyPage(Page):
    body = StreamField(
        [('PrivacyPolicy', PrivacyPolicyBlock()),
         ('ContactusTesimonial', ContactUsTestimonialBlock()),

        ], null = True)
    
    body_panels = [FieldPanel('body')]

    edit_handler = TabbedInterface([
        ObjectList(Page.content_panels, heading= 'Content'),
        ObjectList(body_panels, heading= 'Body'),
        ObjectList(Page.promote_panels, heading='Promote'),
    ])

class CustomServicesPage(Page):
    body = StreamField(
        [('herosection', ServicesHeroSectionBlock()),
         ('ourmission', OurMissionBlock()),
         ('ourvision', OurVisionBlock()),
         ('ourvalues', OurValuesBlock()),
         ('ourjourney', OurJourneyBlock()),
         ('ourgallery', OurGalleryBlock()),
         ('ourtestimonial', OurTestimonialBlock()),
         ('blogsherosection', BlogsHerosection()),
         ('blogswrapper', BlogsWrapperBlock()),

        ], null = True)
    
    body_panels = [FieldPanel('body')]

    edit_handler = TabbedInterface([
        ObjectList(Page.content_panels, heading= 'Content'),
        ObjectList(body_panels, heading= 'Body'),
        ObjectList(Page.promote_panels, heading='Promote'),
    ])