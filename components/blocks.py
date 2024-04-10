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

class PrimaryButtonBlock(StructBlock): 
    title = CharBlock(classname = "title", required = True)
    icon = ImageChooserBlock(required = False)
    link = PageChooserBlock(can_choose_root= True)

    class Meta:
        min_num = 0
        max_num = 1
        template = "basic_blocks/primary_button.html"

class HeroTitleBlock(StructBlock):
    title = CharBlock(classname="title", required=True)
    subtitle = CharBlock(classname="subtitle", required=True)

class HeroSectionBlock(StructBlock):
    titles = StreamBlock([('title', HeroTitleBlock())])
    include_quick_testimonials = BooleanBlock(required=False)
    primary_button = StreamBlock([('button', PrimaryButtonBlock())])
    image_cover = ImageChooserBlock(required=False)
    image_decor = ImageChooserBlock(required= False)
    class Meta:
        icon = "title"
        template = "blocks/herosection.html"




class OurMissionBlock(StructBlock):
    title = CharBlock(classname="title", required=True)
    subtitle = CharBlock(classname="subtitle", required=True)
    cover_image = ImageChooserBlock(required=False)

    class Meta: 
        template = "blocks/ourmission.html"


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


class OurValuesBlock(StructBlock):
    title = CharBlock(classname='title', required=True)
    word1 = CharBlock(classname='word1', required=True)
    word2 = CharBlock(classname='word2', required=True)
    word3 = CharBlock(classname='word3', required=True)
    word4 = CharBlock(classname='word4', required=True)
    word5 = CharBlock(classname='word5', required=True)

    class Meta:
        template = "blocks/ourvalues.html"


class OurJourneyCard(StructBlock):
    image = ImageChooserBlock(required = False)
    title = CharBlock(classname = "title", required=True)
    subtitle = CharBlock(classname = "subtitle", required=True)

class OurJourneyBlock(StructBlock):
    title = CharBlock(classname="title", required=True)
    subtitle = CharBlock(classname="subtitle", required=True)
    ourjourneycards = StreamBlock([('ourjourneycard', OurJourneyCard())])

    class Meta:
        template = "blocks/ourjourney.html"




class OurGalleryBlock(StructBlock):
    title = CharBlock(classname="title", required=True)
    gallery = StreamBlock([('gallery', ListBlock(ImageChooserBlock()))])

    class Meta:
        template = "blocks/ourgallery.html"



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

class BlogsWrapperCard(StructBlock):
    image = ImageChooserBlock(required = False)
    title = CharBlock(classname="title", required=True)
    category = CharBlock(classname="subtitle", required=True)
    info = CharBlock(classname="subtitle", required=True)


class BlogsWrapperBlock(StructBlock):
    title = CharBlock(classname="title", required=True)
    cards = StreamBlock([('blogswrappercard', BlogsWrapperCard())])

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

class ImageTitleCombo(StructBlock):
    title = CharBlock(classname="title", required=True)
    image = ImageChooserBlock(required=True)

class OneColScrollerSection(StructBlock):
    title = CharBlock(classname="title", required=True)
    subtitle = CharBlock(classname="subtitle", required=True)
    content = CharBlock(classname="subtitle", required=True)
    cards = StreamBlock([('image', ImageTitleCombo())])

    class Meta:
        template = "blocks/onecolscrollersection.html"