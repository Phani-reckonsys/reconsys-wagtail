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
    ChoiceBlock
)
from wagtail.models import StreamField
from wagtail.embeds.blocks import EmbedBlock
from wagtail.images.blocks import ImageChooserBlock


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
    include_fullimage = BooleanBlock(required=False)
    image_cover = ImageChooserBlock(required = False)
    image_decor = ImageChooserBlock(required = False)

#BlogsCard Basic Block
class BlogsCard(StructBlock):
    image = ImageChooserBlock(required = False)
    title = CharBlock(classname="title", required=True)
    category = CharBlock(classname="category", required=True)
    info = CharBlock(classname="info", required=True)
    link = URLBlock(classname="link", required=True)

#ImageTitle Combo Basic Block
class ImageTitleCombo(StructBlock):
    title = CharBlock(classname="title", required=True)
    image = ImageChooserBlock(required=True)

#Testimonial Card Basic Block
class TestimonialCard(StructBlock):
    review = CharBlock(classname="title", required=True)
    name = CharBlock(classname="title", required=True)
    designation = CharBlock(classname="title", required=True)

class Image(StructBlock):
    image = ImageChooserBlock(required=False)

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

#----------Basic Blocks Ends------------------


#-----------Main Blocks Starts----------------

#Herosection Block
class HeroSectionBlock(StructBlock):
    sidetitle = CharBlock(classname="title", required=True)
    content = StreamBlock([('herocontent', HeroContentBasicBlock())])
    # primary_button = StreamBlock([('button', PrimaryButtonBlock())])
    include_companies = BooleanBlock(required=False)
    company_image = StreamBlock([('image', Image())], required=False)
    # image_cover = ImageChooserBlock(required=False)
    # image_decor = ImageChooserBlock(required= False)
    

    class Meta:
        icon = "title"
        template = "blocks/herosection.html"

# HomePage Testimonail section
class HomeTestimonialsBlock(StructBlock):
    sidetitle = CharBlock(classname="title", required=True)
    title = CharBlock(classname="title", required=True)
    subtitle = CharBlock(classname="title", required=True)

    testimonialcards = StreamBlock([('testimonialcard', TestimonialCard())])
    ratingcards = StreamBlock([('ratingcard', RatingCard())])

    class Meta:
        template = "blocks/hometestimonials.html"

class RatingBlock(StructBlock):
    sidetitle = CharBlock(classname="title", required=True)
    title = CharBlock(classname="title", required=True)
    ratingcards = StreamBlock([('ratingcard2', RatingCard2()), ('badge', Image())])
    badgecards = StreamBlock([('badge', Image())])

    class Meta: 
        template = "blocks/rating.html"

# HomePage Blogs Section
class HomeBlogsBlock(StructBlock):
    sidetitle = CharBlock(classname="title", required=True)
    title = CharBlock(classname="title", required=True)
    subtitle = CharBlock(classname="title", required=True)
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
    subtitle = CharBlock(classname="subtitle", required=True)
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
    subtitle = CharBlock(classname="subtitle", required=True)
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
    content = CharBlock(classname="content", required=True)
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
    title = CharBlock(classname="title", required=True)
    cards = StreamBlock([('blogswrappercard', BlogsCard())])

    class Meta: 
        template = "blocks/blogswrapper.html"

#Cover Image Block
class CoverImageBlock(StructBlock):
    image = ImageChooserBlock(required = False)

    class Meta: 
        template = "blocks/coverimage.html"

#Culture Block
class CultureBlock(StructBlock):
    sidetitle = CharBlock(classname="title", required=True)
    title = CharBlock(classname="title", required=True)
    subtitle = CharBlock(classname="subtitle", required=True)
    gallery = StreamBlock([('gallery', ListBlock(ImageChooserBlock()))])

    class Meta:
        template = "blocks/culture.html"

#One Column Scroller Block
class OneColScrollerSection(StructBlock):
    sidetitle = CharBlock(classname="title", required=True)
    title = CharBlock(classname="title", required=True)
    subtitle = CharBlock(classname="subtitle", required=True)
    btntitle = CharBlock(classname="subtitle", required=True)
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
    subtitle = CharBlock(classname="subtitle", required=True)
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
    subtitle =CharBlock(clasname="title", required=True)
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
    title = CharBlock(classname="title", required=True)
    subtitle = CharBlock(classname="title", required=True)
    categorytitles = StreamBlock([("TitleTabCombo", TitleTagCombo())])
    cards = StreamBlock([("OurWorkCards", OurWorkCard())])
    btntitle = CharBlock(classname="title", required=True)
    icon = ImageChooserBlock(required=False)
    outlinegrey_button = StreamBlock([('button', OutlineGreyButtonBlock())])
    class Meta:
        template = "blocks/ourworksdisplay.html"

class ContactUsTestimonialBlock(StructBlock):
    clutch_logo = ImageChooserBlock(required=False)
    testimonialcards = StreamBlock([('testimonialcard', TestimonialCard())])

    class Meta:
        template = "blocks/contactustestimonial.html"

class ContactUsBlock(StructBlock):
    title = CharBlock(classname="title", required=True)
    subtitle = CharBlock(classname="subtitle", required=True)
    optiontext = StreamBlock([('optiontext', Text())])

    class Meta:
        template = "blocks/contactusblock.html"

class ThankyouBlock(StructBlock):
    title = CharBlock(classname="title", required=True)
    subtitle = CharBlock(classname="subtitle", required=True)
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
    title = CharBlock(classname="title", required=True)
    badgefield = StreamBlock([('image', Image())])


    class Meta: 
        template = "blocks/badges.html"