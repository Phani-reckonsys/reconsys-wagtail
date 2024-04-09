from wagtail.blocks import (
    CharBlock,
    ChoiceBlock,
    RichTextBlock,
    StreamBlock,
    StructBlock,
    BooleanBlock
)
from wagtail.models import StreamField
from wagtail.embeds.blocks import EmbedBlock
from wagtail.images.blocks import ImageChooserBlock



class HeroTitleBlock(StructBlock):
    title = CharBlock(classname="title", required=True)
    subtitle = CharBlock(classname="subtitle", required=True)

class HeroSectionBlock(StructBlock):
    titles = StreamBlock([('title', HeroTitleBlock())])
    include_quick_testimonials = BooleanBlock(required=False)

    class Meta:
        icon = "title"
        template = "blocks/herosection.html"