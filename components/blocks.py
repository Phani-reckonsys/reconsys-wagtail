from wagtail.blocks import (
    CharBlock,
    ChoiceBlock,
    RichTextBlock,
    StreamBlock,
    StructBlock,
    BooleanBlock,
    PageChooserBlock,
    ListBlock,
    URLBlock,
    ChoiceBlock,
    
)
from wagtail.models import StreamField
from wagtail.embeds.blocks import EmbedBlock
from wagtail.images.blocks import ImageChooserBlock
from wagtail.contrib.table_block.blocks import TableBlock


#-----------Basic Blocks Starts------------
#Primary button Basic Block
class PrimaryButtonBlock(StructBlock): 
    title = CharBlock(classname = "title", required = True)
    icon = ImageChooserBlock(required = False)
    link = PageChooserBlock(can_choose_root= True, required = False)

    class Meta:
        min_num = 0
        max_num = 1
        template = "basic_blocks/primary_button.html"

#Outline button Basic Block
class OutlineGreyButtonBlock(StructBlock): 
    title = CharBlock(classname = "title", required = True)
    icon = ImageChooserBlock(required = False)
    link = PageChooserBlock(can_choose_root= True, required = False )

    class Meta:
        template = "basic_blocks/outline_grey_button.html"

#Card Basic Block
class CardBasicBlock(StructBlock):
    image = ImageChooserBlock(required = False)
    title = CharBlock(classname = "title", required=True)
    subtitle = CharBlock(classname = "subtitle", required=True)
    blog_link = PageChooserBlock(can_choose_root= True, required = False )

#TitleGroup Basic Block
class TitleGroupBasicBlock(StructBlock):
    title = CharBlock(classname="title", required=True)
    subtitle = CharBlock(classname="subtitle", required=True)

#herosection content Block
class HeroContentBasicBlock(StructBlock):
    title = CharBlock(classname="title", required=True)
    subtitle = CharBlock(classname="subtitle", required=True)
    btn_title = CharBlock(classname = "title", required = True)
    btn_icon = ImageChooserBlock(required = False)
    btn_link = PageChooserBlock(can_choose_root= True)
    btn_url_link = URLBlock(classname="link", required=False)
    include_fullimage = BooleanBlock(required=False)
    include_url_button = BooleanBlock(required = False)
    image_cover = CharBlock(classname = "imagecover", required=False)
    image_decor = CharBlock(classname = "imagedecor", required=False)

#BlogsCard Basic Block
class BlogsCard(StructBlock):
    image = ImageChooserBlock(required = False)
    title = CharBlock(classname="title", required=True)
    category = CharBlock(classname="category", required=True)
    info = CharBlock(classname="info", required=True)
    pagelink = PageChooserBlock(can_choose_root= True, required=False)

#ImageTitle Combo Basic Block
class ImageTitleCombo(StructBlock):
    title = CharBlock(classname="title", required=True)
    image = ImageChooserBlock(required=True)

#Testimonial Card Basic Block
class TestimonialCard(StructBlock):
    avatar = ImageChooserBlock(required=False)
    review = CharBlock(classname="title", required=True)
    name = CharBlock(classname="title", required=True)
    designation = CharBlock(classname="title", required=True)

class Image(StructBlock):
    image = ImageChooserBlock(required=False)

class CustomImage(StructBlock):
    image = ImageChooserBlock(required=False)
    width = CharBlock(classname="width", required=False)

    class Meta:
        template="basic_blocks/image_basic_block.html"

class Text(StructBlock):
    text = CharBlock(classname="title", required=True)

class RatingCard(StructBlock):
    star1 = ImageChooserBlock(required= False)
    star2 = ImageChooserBlock(required= False)
    star3 = ImageChooserBlock(required= False)
    star4 = ImageChooserBlock(required= False)
    star5 = ImageChooserBlock(required= False)
    url = URLBlock(classname="link", required=True)
    rating = CharBlock(classname="title", required=True)
    review_count = CharBlock(classname="title", required=True)
    logo = ImageChooserBlock(required= False)

class RatingCard2(StructBlock):
    star1 = ImageChooserBlock(required= False)
    star2 = ImageChooserBlock(required= False)
    star3 = ImageChooserBlock(required= False)
    star4 = ImageChooserBlock(required= False)
    star5 = ImageChooserBlock(required= False)
    url = URLBlock(classname="link", required=True)
    rating = RichTextBlock(classname="title", required=True)
    logo = ImageChooserBlock(required= False)

class AccordionBasic(StructBlock):
    question = CharBlock(classname="question", required= False)
    answer = CharBlock(classname="answer", required=False)
    service_icon = ImageChooserBlock(required = False)

class StatBasic(StructBlock):
    title = CharBlock(classname="title", required=False)
    data = CharBlock(classname="data", required=False)

class ListBasic(StructBlock):
    number = CharBlock(classname="number", required=False)
    content = CharBlock(classname="content", required=False)

class CasestudyCardBasic(StructBlock):
    title = CharBlock(classname="title", required=True)
    subtitle = CharBlock(classname="subtitle", required=True)
    data1 = CharBlock(classname ="data1", required=False)
    label1 = CharBlock(classname = "value1", required=False)
    data2 = CharBlock(classname = "data2", required=False)
    label2 = CharBlock(classname ="value2", required=False)
    cover_image = ImageChooserBlock(required = False)
    bgcolor = CharBlock(classname = "bgcolor", required = False)

class FaqBasicBlock(StructBlock):
    question = CharBlock(classname="question", required=False)
    answer = CharBlock(classname="answer", required=False)

class ServicesBasicCard(StructBlock):
    icon = ImageChooserBlock(required=False)
    title = CharBlock(classname="title", required=False)
    content = CharBlock(classname="content", required=False)

class ServicesTextCard(StructBlock):
    number = CharBlock(classname="number", required=False)
    include_icon = BooleanBlock(required=False)
    icon = ImageChooserBlock(required = False)
    title = CharBlock(classname="title", required=False)
    content = CharBlock(classname="content", required=False)

class CustomServicesBasicCard(StructBlock):
    icon = ImageChooserBlock(required=False)
    background = CharBlock(classname="background", required=False)
    width = CharBlock(classname="width", required=False)
    padding_top = CharBlock(classname="padding_top", required=False)
    padding_right = CharBlock(classname="padding_right", required=False)
    padding_bottom = CharBlock(classname="padding_bottom", required=False)
    padding_left = CharBlock(classname = "padding_left", required=False)
    title = CharBlock(classname="title", required=False)
    content = CharBlock(classname="content", required=False)

class MultipleBasicImageTitle(StructBlock):
    title = CharBlock(classname="title", required=False)
    tooltip = StreamBlock([('imagetitlecombo', ImageTitleCombo())], required=False)

class Uiuxparallaxcard(StructBlock):
    title = CharBlock(classname = "title", required=False)
    subtitle = CharBlock(classname = "title", required=False)
    number_image = CharBlock(classname="numberimage",required=False)
    main_image = ImageChooserBlock(required=False)
    decor_image = ImageChooserBlock(required=False)

class CustomisedSolutionCard(StructBlock):
    icon = ImageChooserBlock(required = False)
    title = CharBlock(classname = "title", required=False)
    subtitle = CharBlock(classname = "subtitle", required=False)
    content = CharBlock(classname = "content", required=False)

#----------Basic Blocks Ends------------------


#-----------Main Blocks Starts----------------

#Herosection Block
class HeroSectionBlock(StructBlock):
    sidetitle = CharBlock(classname="title", required=True)
    content = StreamBlock([('herocontent', HeroContentBasicBlock())])
    include_companies = BooleanBlock(required=False)
    company_image = StreamBlock([('image', Image())], required=False)
    
    class Meta:
        icon = "title"
        template = "blocks/herosection.html"

# HomePage Testimonail section
class HomeTestimonialsBlock(StructBlock):
    sidetitle = CharBlock(classname="title", required=True)
    title = CharBlock(classname="title", required=True)
    subtitle = RichTextBlock(classname="title", required=True)
    testimonialcards = StreamBlock([('testimonialcard', TestimonialCard())])
    ratingcards = StreamBlock([('ratingcard', RatingCard())])

    class Meta:
        template = "blocks/hometestimonials.html"

class RatingBlock(StructBlock):
    sidetitle = CharBlock(classname="title", required=True)
    title = RichTextBlock(classname="title", required=True)
    ratingcards = StreamBlock([('ratingcard2', RatingCard2()), ('badge', Image())])
    badgecards = StreamBlock([('badge', Image())])

    class Meta: 
        template = "blocks/rating.html"

# HomePage Blogs Section
class HomeBlogsBlock(StructBlock):
    sidetitle = CharBlock(classname="title", required=True)
    title = CharBlock(classname="title", required=True)
    subtitle = RichTextBlock(classname="title", required=True)
    blogspagelink = PageChooserBlock(can_choose_root= True, required=False)
    blogcard = StreamBlock([('blogcard', BlogsCard())])


    class Meta:
        template = "blocks/homeblogs.html"

    

#OurMission Block
class OurMissionBlock(StructBlock):
    sidetitle = CharBlock(classname="title", required=True)
    title = CharBlock(classname="title", required=True)
    subtitle = RichTextBlock(classname="subtitle", required=True)
    cover_image = ImageChooserBlock(required=False)

    class Meta: 
        template = "blocks/ourmission.html"

#OurVision Block
class OurVisionBlock(StructBlock):
    sidetitle = CharBlock(classname="title", required=True)
    title = CharBlock(classname="title", required=True)
    subtitle = RichTextBlock(classname="subtitle", required=True)
    cover_image = ImageChooserBlock(required=False)
    image1 = ImageChooserBlock(required=False)
    image2 = ImageChooserBlock(required=False)
    image3 = ImageChooserBlock(required=False)
    image4 = ImageChooserBlock(required=False)
    image5 = ImageChooserBlock(required=False)
    image6 = ImageChooserBlock(required=False)

    class Meta: 
        template = "blocks/ourvision.html"

#OurValues Block
class OurValuesBlock(StructBlock):
    sidetitle = CharBlock(classname='title', required=True)
    title = CharBlock(classname='title', required=True)
    word1 = CharBlock(classname='word1', required=True)
    word2 = CharBlock(classname='word2', required=True)
    word3 = CharBlock(classname='word3', required=True)
    word4 = CharBlock(classname='word4', required=True)
    word5 = CharBlock(classname='word5', required=True)

    class Meta:
        template = "blocks/ourvalues.html"


#OurJourney Block
class OurJourneyBlock(StructBlock):
    sidetitle = CharBlock(classname="title", required=True)
    title = CharBlock(classname="title", required=True)
    subtitle = RichTextBlock(classname="subtitle", required=True)
    ourjourneycards = StreamBlock([('ourjourneycard', CardBasicBlock())])

    class Meta:
        template = "blocks/ourjourney.html"

#OurGallery Block
class OurGalleryBlock(StructBlock):
    sidetitle = CharBlock(classname="title", required=True)
    title = CharBlock(classname="title", required=True)
    gallery = StreamBlock([('gallery', ListBlock(ImageChooserBlock()))])

    class Meta:
        template = "blocks/ourgallery.html"

#OurTestimonial Block
class OurTestimonialBlock(StructBlock):
    sidetitle = CharBlock(classname="content", required=True)
    name = CharBlock(classname="content", required=True)
    designation = CharBlock(classname="content", required=True)
    image = ImageChooserBlock(required = False)
    content = RichTextBlock(classname="content", required=True)
    svg = ImageChooserBlock(required = False)

    
    class Meta: 
        template = "blocks/ourtestimonial.html"

#OurTestimonial Block
class TestimonialGenericBlock(StructBlock):
    sidetitle = CharBlock(classname="content", required=True)
    name = CharBlock(classname="content", required=True)
    designation = CharBlock(classname="content", required=True)
    image = ImageChooserBlock(required = False)
    content = CharBlock(classname="content", required=True)
    svg = ImageChooserBlock(required = False)
    bgcolor = CharBlock(classname="bgcolor", required=True)
    fontcolor = CharBlock(classname="bgcolor", required=True)
    
    class Meta: 
        template = "blocks/testimonialgeneric.html"

#Herosection Blogs Page Block
class BlogsHerosection(StructBlock):
    sidetitle = CharBlock(classname="title", required=True)
    title = CharBlock(classname="title", required=True)
    subtitle = CharBlock(classname="subtitle", required=True)
    cards = StreamBlock([('blogsherosectioncards', CardBasicBlock())])

    class Meta: 
        template = "blocks/blogsherosection.html"

#Blogs container Section Block
class BlogsWrapperBlock(StructBlock):
    sidetitle = CharBlock(classname="title", required=True)
    title = RichTextBlock(classname="title", required=True)
    cards = StreamBlock([('blogswrappercard', BlogsCard())])

    class Meta: 
        template = "blocks/blogswrapper.html"

#Cover Image Block
class CoverImageBlock(StructBlock):
    backgroundcolor = CharBlock(classname="backgroundcolor", required=False)
    image = ImageChooserBlock(required = False)

    class Meta: 
        template = "blocks/coverimage.html"

#Culture Block
class CultureBlock(StructBlock):
    sidetitle = CharBlock(classname="title", required=True)
    title = CharBlock(classname="title", required=True)
    subtitle = RichTextBlock(classname="subtitle", required=True)
    content = RichTextBlock(classname="content", required=False)
    gallery = StreamBlock([('gallery', ListBlock(ImageChooserBlock()))])

    class Meta:
        template = "blocks/culture.html"

#One Column Scroller Block
class OneColScrollerSection(StructBlock):
    sidetitle = CharBlock(classname="title", required=True)
    title = CharBlock(classname="title", required=True)
    subtitle = RichTextBlock(classname="subtitle", required=True)
    content = CharBlock(classname="subtitle", required=True)
    cards = StreamBlock([('image', ImageTitleCombo())])
    url = URLBlock(classname="link", required=True)
    btntext = CharBlock(classname="subtitle", required=True)

    class Meta:
        template = "blocks/onecolscrollersection.html"

#Benifits Grid Block
class BenifitsBlock(StructBlock):
    sidetitle = CharBlock(classname="title", required=True)
    title = CharBlock(classname="title", required=True)
    subtitle = RichTextBlock(classname="subtitle", required=True)
    cards = StreamBlock([('Benifitcard', CardBasicBlock())])
    
    class Meta:
        template = "blocks/benifitsgrid.html"

#OurWorks Herosection Block
class OurWorksHerosectionBlock(StructBlock):
    sidetitle = CharBlock(classname="title", required=True)
    title = CharBlock(classname="title", required=True)
    subtitle = CharBlock(classname="title", required=True)
    content = CharBlock(classname="title", required=True)
    primary_button = StreamBlock([('button', PrimaryButtonBlock())])
    image = ImageChooserBlock(required=False)

    class Meta: 
        template = "blocks/ourworksherosection.html"


class OurWorkCard(StructBlock):
    title =CharBlock(clasname="title", required=True)
    tag = ChoiceBlock(choices=[
    ('csd', 'Custom Sofware Development'),
    ('ui', 'UI/UX Design'),
    ], icon='cup')
    subtitle = CharBlock(clasname="title", required=True)
    label1 =CharBlock(clasname="data title 1", required=True)
    label2 =CharBlock(clasname="data title 2", required=True)
    data1 =CharBlock(clasname="data1", required=True)
    data2 =CharBlock(clasname="data2", required=True)
    image =ImageChooserBlock(required=False)
    bgcolor = CharBlock(clasname="BackgroundColor", required=True)

class TitleTagCombo(StructBlock):
    title =CharBlock(clasname="title", required=True)
    tag = ChoiceBlock(choices=[
    ('csd-btn', 'Custom Sofware Development'),
    ('ui-btn', 'UI/UX Design'),
    ('all-btn', 'All')
    ], icon='cup')

#OurWorks Display
class OurWorksDisplayBlock(StructBlock):
    sidetitle = CharBlock(classname="title", required=True)
    title = RichTextBlock(classname="title", required=True)
    subtitle = CharBlock(classname="title", required=True)
    categorytitles = StreamBlock([("TitleTabCombo", TitleTagCombo())])
    cards = StreamBlock([("OurWorkCards", OurWorkCard())])
    btntitle = CharBlock(classname="title", required=True)
    class Meta:
        template = "blocks/ourworksdisplay.html"

class ContactUsTestimonialBlock(StructBlock):
    clutch_logo = ImageChooserBlock(required=False)
    testimonialcards = StreamBlock([('testimonialcard', TestimonialCard())])

    class Meta:
        template = "blocks/contactustestimonial.html"

class ContactUsBlock(StructBlock):
    title = CharBlock(classname="title", required=True)
    subtitle = RichTextBlock(classname="subtitle", required=True)
    optiontext = StreamBlock([('optiontext', Text())])

    class Meta:
        template = "blocks/contactusblock.html"

class ThankyouBlock(StructBlock):
    custom_head  = RichTextBlock(help_text="Custom HTML to be included in the <head> section")
    title = CharBlock(classname="title", required=True)
    subtitle = RichTextBlock(classname="subtitle", required=True)
    image_cover = ImageChooserBlock(required = False)
    image_decor = ImageChooserBlock(required = False)
    class Meta:
        template = "blocks/thankyoublock.html"

class ContactModelBlock(StructBlock):
    close_btn = ImageChooserBlock(required=False)
    title = CharBlock(classname="title", required=True)
    
    class Meta:
        template = "blocks/contactmodel.html"

class EditTextBasicBlock(StructBlock):
    edittext = RichTextBlock(classname="subtitle", required=True)

class PrivacyPolicyBlock(StructBlock):
    sidetitle = CharBlock(classname="sidetitle", required=True)
    title = CharBlock(classname="title", required=True)
    datetitle = CharBlock(classname="lastupdatedtitle", required=True)
    date = CharBlock(classname="date", required=True)
    welcomeline = CharBlock(classname="date", required=True)
    commitment = CharBlock(classname="date", required=True)
    mainimage = ImageChooserBlock(required=False)
    decorimage = ImageChooserBlock(required=False)
    edittextfield = StreamBlock([('edittext', EditTextBasicBlock())])

    class Meta: 
        template = "blocks/privacypolicy.html"

class BadgesBlock(StructBlock):
    title = RichTextBlock(classname="title", required=True)
    badgefield = StreamBlock([('image', Image())])


    class Meta: 
        template = "blocks/badges.html"


class BlogHeaderBlock(StructBlock):
    blogs_url = PageChooserBlock(required=False)
    page_title = CharBlock(classname="title", required=True)
    headline = CharBlock(classname="title", required=True)
    category_title = CharBlock(classname="title", required=True)
    publish_date = CharBlock(classname="title", required=True)
    cover_image = ImageChooserBlock(required=False)
    tags = StreamBlock([('tags', Text())])


    class Meta: 
        template = "blocks/blogheader.html"
new_table_options = {
    'contextMenu': [
        'row_above',
        'row_below',
        '---------',
        'col_left',
        'col_right',
        '---------',
        'remove_row',
        'remove_col',
        '---------',
        'undo',
        'redo',
        '---------',
        'copy',
        'cut',
        '---------',
        'alignment',
    ],
}
class CustomRichTextBlock(StructBlock):
    blog_text = RichTextBlock(classname="title", required=True, features=['h2', 'h3' , 'h4' , 'p' , 'bold', 'hr', 'italic','code','ol','ul','link','image','blockquote'])
    
    class Meta:
        template = "basic_blocks/richtext_block.html"

class TableBlock(StructBlock): 
    table = TableBlock(table_options=new_table_options, required=False)

    class Meta:
        template = "basic_blocks/table_block.html"
    

class BlogTabledBody(StructBlock):
    profile_image = ImageChooserBlock(required=False)
    name = CharBlock(classname="title", required=True)
    designation = CharBlock(classname="title", required=True)
    about_the_author = CharBlock(classname="title", required=True)
    twitter_url = URLBlock(classname="link", required=False)
    linkedin_url = URLBlock(classname="link", required=False)
    facebook_url = URLBlock(classname="link", required=False)
    url = URLBlock(classname="link", required=True)
    blog_text = StreamBlock([('richtext', RichTextBlock()), ('tableblock', TableBlock()), ('image', CustomImage())])
    
    class Meta: 
        template = "blocks/blogtabledbody.html"

class BlogBodyBlock(StructBlock):
    profile_image = ImageChooserBlock(required=False)
    name = CharBlock(classname="title", required=True)
    designation = CharBlock(classname="title", required=True)
    about_the_author = CharBlock(classname="title", required=True)
    twitter_url = URLBlock(classname="link", required=False)
    linkedin_url = URLBlock(classname="link", required=False)
    facebook_url = URLBlock(classname="link", required=False)
    url = URLBlock(classname="link", required=True)
    blog_content = StreamBlock([('richtext', CustomRichTextBlock()), ('tableblock', TableBlock()), ('image', CustomImage()) ])

    class Meta:
        template = "blocks/blogbody.html"


class ServicesHeroSectionBlock(StructBlock):
    parentpage = CharBlock(classname="parentpage", required=False)
    sidetitle = CharBlock(classname="sidetitle", required=True)
    title = CharBlock(classname="title", required=True)
    services_url = PageChooserBlock(required = False)
    subtitle = CharBlock(classname="subtitle", required=True)
    btn_title = CharBlock(classname = "title", required = True)
    btn_icon = ImageChooserBlock(required = False)
    btn_link = PageChooserBlock(can_choose_root= True)
    btn_url_link = URLBlock(classname="link", required=False)
    include_fullimage = BooleanBlock(required=False)
    include_url_button = BooleanBlock(required = False)
    image_cover = CharBlock(classname = "imagecover", required=False)
    image_decor = CharBlock(classname = "imagedecor", required=False)
    include_companies = BooleanBlock(required=False)
    company_image = StreamBlock([('image', Image())], required=False)
    

    class Meta:
        icon = "title"
        template = "blocks/services_herosection.html"

class ServicesofferedBlock(StructBlock):
    sidetitle = CharBlock(classname="sidetitle", required=False)
    title = CharBlock(classname="title", required=False)
    content = RichTextBlock(classname="content", required=False)
    accordion = StreamBlock([('accordionbasic', AccordionBasic())], required=False)
    
    class Meta:
        icon = "title"
        template = "blocks/servicesoffered.html"

class ServicesDatasectionBlock(StructBlock):
    sidetitle = CharBlock(classname="sidetitle", required=False)
    content = RichTextBlock(classname="contnet", required=False)
    stat = StreamBlock([('statbasic', StatBasic())], required=False)

    class Meta:
        template = "blocks/services_datasection.html"


class ServicesWhychooseusBlock(StructBlock):
    sidetitle = CharBlock(classname="sidetitle", required=False)
    title = CharBlock(classname = "title", required=False)
    content = RichTextBlock(classname = "content", required=False)
    list = StreamBlock([('listbasic', ListBasic())], required=False)

    class Meta: 
        template = "blocks/services_whychooseus.html"

class ServicesCasestudiesBlock(StructBlock):
    sidetitle = CharBlock(classname="sidetitle", required=False)
    title = CharBlock(classname="title", required=False)
    content = RichTextBlock(classname = "content", required=False)
    removebuttons = BooleanBlock(required=False)
    card = StreamBlock([('casestudycardbasic', CasestudyCardBasic())], required=False)
    
    class Meta:
        template = "blocks/services_casestudies.html"

class FaqBlock(StructBlock):
    sidetitle = CharBlock(classname="sidetitle", required=False)
    bordercolor = CharBlock(classname="bordercolor", required=False)
    backgroundcolor = CharBlock(classname="backgroundcolor", required=False)
    color = CharBlock(classname="backgroundcolor", required=False)
    maintitle = CharBlock(classname="title", required=False)
    title = RichTextBlock(classname="title", required=False)
    faq = StreamBlock([('faqbasicblock', FaqBasicBlock())], required=False)

    class Meta:
        template = "blocks/faq.html"

class CollaborateBlock(StructBlock):
    backgroundcolor = CharBlock(classname="backgroundcolor", required=False)
    bordercolor = CharBlock(classname="bordercolor", required=False)
    maintextcolor = CharBlock(classname="maintextcolor", required=False)
    sidetitle = CharBlock(classname="sidetitle", required=False)
    image = ImageChooserBlock(required=False)
    title = RichTextBlock(classname="title", required=False)
    button = StreamBlock([('primarybutton', PrimaryButtonBlock())], required=False)

    class Meta:
        template = "blocks/collaborate.html"


class OurServicesBlock(StructBlock):
    sidetitle = CharBlock(classname ="sidetitle", required=False)
    title = CharBlock(classname= "title", required=False)
    subtitle = RichTextBlock(classname="subtitle", required=False)
    content = CharBlock(classname="content", required=False)
    card = StreamBlock([('servicesbasiccard',ServicesBasicCard())], required=False)

    class Meta:
        template = "blocks/ourservices.html"


class TechnologiesusedBlock(StructBlock):
    backgroundcolor = CharBlock(classname = "backgroundcolor", required=False)
    color = CharBlock(classname = "color", required=False)
    bordercolor = CharBlock(classname="bordercolor", required=False)
    title = CharBlock(classname="title", required=False)
    subtitle = CharBlock(classname="subtitle", required=False)
    tooltipgroup = StreamBlock([('multiplebasicimagetitle', MultipleBasicImageTitle())],required=False)

    class Meta:
        template = "blocks/technologiesused.html"

class EngagmentBlock(StructBlock):
    sidetitle = CharBlock(classname = "sidetitle", required=False)
    title = CharBlock(classname="title", required=False)
    subtitle = RichTextBlock(classname="subtitle", required=False)
    content = CharBlock(classname="content", required=False)
    card = StreamBlock([('servicesbasiccard', ServicesBasicCard())], requried=False)

    class Meta:
        template = "blocks/engagment.html"

class CardscrollerBlock(StructBlock):
    bordercolor = CharBlock(classname="bordercolor", required=False)
    sidetitle = CharBlock(classname="sidetitle", required=False)
    sidebar_background = CharBlock(classname="", required=False)
    title = CharBlock(classname="title", required=False)
    subtitle = RichTextBlock(classname="subtitle", required=False)
    include_buttons = BooleanBlock(required=False)
    content = CharBlock(classname="content", required=False)
    container_background = CharBlock(classname="container_background", required=False)
    card = StreamBlock([('servicebasicscard', CustomServicesBasicCard())], required=False)

    class Meta:
        template = "blocks/cardscroller.html"

class ServicesWhyReckonsysBlock(StructBlock):
    backgroundcolor = CharBlock(classname="backgroundcolor", required=False)
    maintextcolor = CharBlock(classname="maintextcolor", required=False)
    bordercolor = CharBlock(classname="bordercolor", required=False)
    sidebar = CharBlock(classname="sidetitle", required=False)
    title = CharBlock(classname="title", required=False)
    subtitle = RichTextBlock(classname="subtitle", required=False)
    content = CharBlock(classname="content", required=False)
    card = StreamBlock([('servicebasiccard', ServicesTextCard())], required=False)

    class Meta:
        template = "blocks/services_whyreckonsys.html"

#OurProcess Block
class OurProcessBlock(StructBlock):
    sidetitle = CharBlock(classname="title", required=True)
    title = CharBlock(classname="title", required=True)
    subtitle = RichTextBlock(classname="subtitle", required=True)
    content = CharBlock(classname="content", required=True)
    ourprocesscards = StreamBlock([('servicebasiccard', ServicesTextCard())])

    class Meta:
        template = "blocks/ourprocess.html"

class OursuccessBlock(StructBlock):
    sidebar = CharBlock(classname="sidetitle", required=False)
    title = CharBlock(classname="title", required=False)
    subtitle = RichTextBlock(classname="subtitle", required=False)
    halfcardtitle1 = CharBlock(classname="halfcardtitle1", required=False)
    data1 = CharBlock(classname="data1", required=False)
    halfcardtitle2 = CharBlock(classname="halfcardtitle", required=False)
    data2 = CharBlock(classname="data2", required=False)
    cardimage = ImageChooserBlock(required=False)
    fullcardtitle1 = CharBlock(classname="fullcardtitle1", required=False)
    data3 = CharBlock(classname="data3", required=False)
    btn_title = CharBlock(classname="btntitle", required=False)
    pagelink = PageChooserBlock(can_choose_root= True, required=False)


    class Meta:
        template = "blocks/oursuccess.html"


class OurmethodologiesBlock(StructBlock):
    sidetitle = CharBlock(classname="sidetitle", reduired=False)
    title = CharBlock(classname="title", required=False)
    subtitle = RichTextBlock(classname="subtitle", required=False)
    content = CharBlock(classname="content", required=False)
    selectors = StreamBlock([("imagetitlecombo", ImageTitleCombo())], required=False)
    contentdisplay = StreamBlock([("imagetitlecombo", ImageTitleCombo())], required=False)

    class Meta:
        template = "blocks/ourmethodologies.html"


class UiuxHerosectionBlock(StructBlock):
    sidetitle = CharBlock(classname="title", required=True)
    title = CharBlock(classname="title", required=True)
    services_url = PageChooserBlock(required = False)
    subtitle = RichTextBlock(classname="subtitle", required=True)
    btn_title = CharBlock(classname = "title", required = True)
    btn_icon = ImageChooserBlock(required = False)
    btn_link = PageChooserBlock(can_choose_root= True)
    btn_url_link = URLBlock(classname="link", required=False)
    include_fullimage = BooleanBlock(required=False)
    include_url_button = BooleanBlock(required = False)
    image_cover = CharBlock(classname = "imagecover", required=False)
    image_decor = CharBlock(classname = "imagedecor", required=False)
    include_companies = BooleanBlock(required=False)
    company_image = StreamBlock([('image', Image())], required=False)
    

    class Meta:
        icon = "title"
        template = "blocks/uiux_herosection.html"

class UiuxWedoBlock(StructBlock):
    title = CharBlock(classname="title", required=False)
    subtitle = RichTextBlock(classname="subtitle", required=False)
    content = CharBlock(classname="content", required=False)
    card = StreamBlock([('uiuxparallaxcard', Uiuxparallaxcard())])

    class Meta:
        icon = "title"
        template = "blocks/uiux_wedo.html"

class UiuxsuccessBlock(StructBlock):
    sidetitle = CharBlock(classname="sidetitle", required=False)
    title = CharBlock(classname="title", required=False)
    content = RichTextBlock(classname = "content", required=False)
    card = StreamBlock([('casestudycardbasic', CasestudyCardBasic())], required=False)
    
    class Meta:
        template = "blocks/uiux_success.html"

class UiuxworkBlock(StructBlock):
    title = CharBlock(classname="title", required=False)
    content = RichTextBlock(classname = "content", required=False)
    points = StreamBlock([('imagetitlecombo', ImageTitleCombo())], required=False)
    
    class Meta:
        template = "blocks/uiux_work.html"

class UiuxtestimonialBlock(StructBlock):
    title = CharBlock(classname="title", required=False)
    testimonialscard = StreamBlock([('testimonialcard', TitleGroupBasicBlock())])

    class Meta:
        template = "blocks/uiux_testimonial.html"


class CsrHerosection(StructBlock):
    sidetitle = CharBlock(classname="title", required=True)
    title = CharBlock(classname="title", required=True)
    subtitle = CharBlock(classname="title", required=False)
    include_fullimage = BooleanBlock(required=False)
    image_cover = CharBlock(classname = "imagecover", required=False)
    image_decor = CharBlock(classname = "imagedecor", required=False)

    class Meta:
        template = "blocks/csrherosection.html"


class TextimageBlock(StructBlock):
    text = RichTextBlock(classname="text", required=False)
    image = ImageChooserBlock(required=False)

    class Meta:
        template = "blocks/textimage.html"

class EmpoweringBlock(StructBlock):
    sidetitle = CharBlock(classname="title", required=True)
    title = CharBlock(classname="title", required=True)
    subtitle = RichTextBlock(classname="subtitle", required=False)
    content = RichTextBlock(classname="content", required=False)
    image = ImageChooserBlock(required=False)

    class Meta:
        template = "blocks/empowering.html"

class CustomisedSolution(StructBlock):
    sidetitle = CharBlock(classname="sidetitle", required=False)
    title = RichTextBlock(classname="title", required=False)
    subtitle = CharBlock(classname="subtitle", required=False)
    cards = StreamBlock([('customisedsolutionscard', CustomisedSolutionCard())])
    url = PageChooserBlock(required=False)
    btntext = CharBlock(classname="subtitle", required=False)

    class Meta:
        template = "blocks/customised_solutions.html"

class ServicesBannerCard(StructBlock):
    image = ImageChooserBlock(required=False)
    title = RichTextBlock(classname="title", required=False)

class ServicesBanner(StructBlock):
    sidetitle = CharBlock(classname = "sidetitle", required=False)
    title = RichTextBlock(classname="title",required=False)
    card = StreamBlock([('servicesbanner', ServicesBannerCard())])

    class Meta:
        template = "blocks/services_banner.html"


class Industrieswhychoose(StructBlock):
    maintitle = CharBlock(classname="maintitle", required=False)
    mainsubtitle = CharBlock(classname="mainsubtitle", required=False)
    image = ImageChooserBlock(required=False)
    title = RichTextBlock(classname="title", required=False)
    subtitle = CharBlock(classname="subtitle", required=False)
    button = StreamBlock([('primarybutton', PrimaryButtonBlock())], required=False)

    class Meta:
        template = "blocks/industrieswhychoose.html"

class Casestudiesherosection(StructBlock):
    ourworks_url = PageChooserBlock(required=False)
    sidetitle = CharBlock(classname="sidetitle", required=False)
    title = CharBlock(classname="title", required=False)
    subtitle = CharBlock(classname="subtitle", required=False)
    image = ImageChooserBlock(required=False)
    sectionmaintitle = CharBlock(classname="sectionmaintitle", required=False)
    sectiontitle1 = CharBlock(classname="sectiontitle1", required=False)
    sectiontitle2 = CharBlock(classname="sectiontitle2", required=False)
    sectiontitle3 = CharBlock(classname="sectiontitle3", required=False)

    class Meta:
        template = "blocks/casestudiesherosection.html"


class Casestudiessinglegrid(StructBlock):
    sidetitle = CharBlock(classname="sidetitle", required=False)
    title = CharBlock(classname="title", required=False)
    subtitle = CharBlock(classname="subtitle", required=False)
    image1 = ImageChooserBlock(required=False)
    image2 = ImageChooserBlock(required=False)

    class Meta:
        template = "blocks/casestudiessinglegrid.html"
