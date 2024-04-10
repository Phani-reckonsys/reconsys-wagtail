from wagtail.blocks import (
    CharBlock,
    ChoiceBlock,
    RichTextBlock,
    StreamBlock,
    StructBlock,
    BooleanBlock,
    PageChooserBlock
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

class Images(StructBlock):
    image = ImageChooserBlock(required=False)

class Gallerys(StreamBlock):
    gallerys = StreamBlock([('images', Images())])


class OurVisionBlock(StructBlock):
    gallery = StreamBlock([('gallerys', Gallerys())])
    title = CharBlock(classname="title", required=True)
    subtitle = CharBlock(classname="subtitle", required=True)

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