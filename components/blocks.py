from wagtail.blocks import (
    CharBlock,
    ChoiceBlock,
    RichTextBlock,
    StreamBlock,
    StructBlock,
    BooleanBlock,
    PageChooserBlock,
    ListBlock
)
from wagtail.models import StreamField
from wagtail.embeds.blocks import EmbedBlock
from wagtail.images.blocks import ImageChooserBlock


#-----------Basic Blocks section------------
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
    category = CharBlock(classname="subtitle", required=True)
    info = CharBlock(classname="subtitle", required=True)

#ImageTitle Combo Basic Block
class ImageTitleCombo(StructBlock):
    title = CharBlock(classname="title", required=True)
    image = ImageChooserBlock(required=True)



#-----------Main Blocks Section Starts--------------

#Herosection Block
class HeroSectionBlock(StructBlock):
    titles = StreamBlock([('title', TitleGroupBasicBlock())])
    include_quick_testimonials = BooleanBlock(required=False)
    primary_button = StreamBlock([('button', PrimaryButtonBlock())])
    image_cover = ImageChooserBlock(required=False)
    image_decor = ImageChooserBlock(required= False)
    class Meta:
        icon = "title"
        template = "blocks/herosection.html"

#OurMission Block
class OurMissionBlock(StructBlock):
    title = CharBlock(classname="title", required=True)
    subtitle = CharBlock(classname="subtitle", required=True)
    cover_image = ImageChooserBlock(required=False)

    class Meta: 
        template = "blocks/ourmission.html"

#OurVision Block
class OurVisionBlock(StructBlock):
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
    title = CharBlock(classname="title", required=True)
    subtitle = CharBlock(classname="subtitle", required=True)
    ourjourneycards = StreamBlock([('ourjourneycard', CardBasicBlock())])

    class Meta:
        template = "blocks/ourjourney.html"

#OurGallery Block
class OurGalleryBlock(StructBlock):
    title = CharBlock(classname="title", required=True)
    gallery = StreamBlock([('gallery', ListBlock(ImageChooserBlock()))])

    class Meta:
        template = "blocks/ourgallery.html"

#OurTestimonial Block
class OurTestimonialBlock(StructBlock):
    image = ImageChooserBlock(required = False)
    content = CharBlock(classname="content", required=True)
    svg = ImageChooserBlock(required = False)
    
    class Meta: 
        template = "blocks/ourtestimonial.html"


class BlogsHerosectionCards(StructBlock):
    image = ImageChooserBlock(required = False)
    title = CharBlock(classname="title", required=True)
    subtitle = CharBlock(classname="subtitle", required=True)


class BlogsHerosection(StructBlock):
    title = CharBlock(classname="title", required=True)
    subtitle = CharBlock(classname="subtitle", required=True)
    cards = StreamBlock([('blogsherosectioncards', BlogsHerosectionCards())])

    class Meta: 
        template = "blocks/blogsherosection.html"


class BlogsWrapperBlock(StructBlock):
    title = CharBlock(classname="title", required=True)
    cards = StreamBlock([('blogswrappercard', BlogsCard())])

    class Meta: 
        template = "blocks/blogswrapper.html"


class CoverImageBlock(StructBlock):
    image = ImageChooserBlock(required = False)

    class Meta: 
        template = "blocks/coverimage.html"

class CultureBlock(StructBlock):
    title = CharBlock(classname="title", required=True)
    subtitle = CharBlock(classname="subtitle", required=True)
    gallery = StreamBlock([('gallery', ListBlock(ImageChooserBlock()))])

    class Meta:
        template = "blocks/culture.html"



class OneColScrollerSection(StructBlock):
    title = CharBlock(classname="title", required=True)
    subtitle = CharBlock(classname="subtitle", required=True)
    content = CharBlock(classname="subtitle", required=True)
    cards = StreamBlock([('image', ImageTitleCombo())])

    class Meta:
        template = "blocks/onecolscrollersection.html"