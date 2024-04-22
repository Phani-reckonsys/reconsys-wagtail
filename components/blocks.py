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
)
from wagtail.models import StreamField
from wagtail.embeds.blocks import EmbedBlock
from wagtail.images.blocks import ImageChooserBlock


#-----------Basic Blocks Starts------------
#Primary button Basic Block
class PrimaryButtonBlock(StructBlock): 
    title = CharBlock(classname = "title", required = True)
    icon = ImageChooserBlock(required = False)
    link = PageChooserBlock(can_choose_root= True)

    class Meta:
        min_num = 0
        max_num = 1
        template = "basic_blocks/primary_button.html"

#Card Basic Block
class CardBasicBlock(StructBlock):
    image = ImageChooserBlock(required = False)
    title = CharBlock(classname = "title", required=True)
    subtitle = CharBlock(classname = "subtitle", required=True)

#TitleGroup Basic Block
class TitleGroupBasicBlock(StructBlock):
    title = CharBlock(classname="title", required=True)
    subtitle = CharBlock(classname="subtitle", required=True)

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
    image = ImageChooserBlock(required=True)

class RatingCard(StructBlock):
    star1 = ImageChooserBlock(required= False)
    star2 = ImageChooserBlock(required= False)
    star3 = ImageChooserBlock(required= False)
    star4 = ImageChooserBlock(required= False)
    star5 = ImageChooserBlock(required= False)
    rating = CharBlock(classname="title", required=True)
    review_count = CharBlock(classname="title", required=True)
    logo = ImageChooserBlock(required= False)

#----------Basic Blocks Ends------------------


#-----------Main Blocks Starts----------------

#Herosection Block
class HeroSectionBlock(StructBlock):
    sidetitles = CharBlock(classname="title", required=True)
    titles = StreamBlock([('title', TitleGroupBasicBlock())])
    include_companies = BooleanBlock(required=False)
    include_fullimage = BooleanBlock(required=False)
    primary_button = StreamBlock([('button', PrimaryButtonBlock())])
    image_cover = ImageChooserBlock(required=False)
    image_decor = ImageChooserBlock(required= False)

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
    subtitle = CharBlock(classname="subtitle", required=True)
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
    image = ImageChooserBlock(required = False)
    content = CharBlock(classname="content", required=True)
    svg = ImageChooserBlock(required = False)
    
    class Meta: 
        template = "blocks/ourtestimonial.html"

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
    content = CharBlock(classname="subtitle", required=True)
    cards = StreamBlock([('image', ImageTitleCombo())])

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
    subtitle =CharBlock(clasname="title", required=True)
    label1 =CharBlock(clasname="data title 1", required=True)
    label2 =CharBlock(clasname="data title 2", required=True)
    data1 =CharBlock(clasname="data1", required=True)
    data2 =CharBlock(clasname="data2", required=True)
    image =ImageChooserBlock(required=False)
    bgcolor = CharBlock(clasname="BackgroundColor", required=True)

#OurWorks Display
class OurWorksDisplayBlock(StructBlock):
    sidetitle = CharBlock(classname="title", required=True)
    title = CharBlock(classname="title", required=True)
    subtitle = CharBlock(classname="title", required=True)
    categorytitles = StreamBlock([("categories", ListBlock(CharBlock()))])
    cards = StreamBlock([("OurWorkCards", OurWorkCard())])

    class Meta:
        template = "blocks/ourworksdisplay.html"

class ContactUsTestimonialBlock(StructBlock):
    clutch_logo = ImageChooserBlock(required=False)
    testimonialcards = StreamBlock([('testimonialcard', TestimonialCard())])

    class Meta:
        template = "blocks/contactustestimonial.html"


class ContactModelBlock(StructBlock):
    close_btn = ImageChooserBlock(required=False)
    title = CharBlock(classname="title", required=True)
    
    class Meta:
        template = "blocks/contactmodel.html"
