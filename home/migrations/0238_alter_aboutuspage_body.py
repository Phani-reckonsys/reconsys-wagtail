# Generated by Django 5.0.7 on 2024-07-30 07:02

import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0237_alter_customservicespage_body_alter_uiuxpage_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutuspage',
            name='body',
            field=wagtail.fields.StreamField([('herosection', wagtail.blocks.StructBlock([('sidetitle', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('content', wagtail.blocks.StreamBlock([('herocontent', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('subtitle', wagtail.blocks.CharBlock(form_classname='subtitle', required=True)), ('btn_title', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('btn_icon', wagtail.images.blocks.ImageChooserBlock(required=False)), ('btn_link', wagtail.blocks.PageChooserBlock(can_choose_root=True)), ('btn_url_link', wagtail.blocks.URLBlock(form_classname='link', required=False)), ('include_fullimage', wagtail.blocks.BooleanBlock(required=False)), ('include_url_button', wagtail.blocks.BooleanBlock(required=False)), ('image_cover', wagtail.blocks.CharBlock(form_classname='imagecover', required=False)), ('image_decor', wagtail.blocks.CharBlock(form_classname='imagedecor', required=False))]))])), ('include_companies', wagtail.blocks.BooleanBlock(required=False)), ('company_image', wagtail.blocks.StreamBlock([('image', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False))]))], required=False))])), ('ourmission', wagtail.blocks.StructBlock([('sidetitle', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('title', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('subtitle', wagtail.blocks.RichTextBlock(form_classname='subtitle', required=True)), ('cover_image', wagtail.images.blocks.ImageChooserBlock(required=False))])), ('ourvision', wagtail.blocks.StructBlock([('sidetitle', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('title', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('subtitle', wagtail.blocks.RichTextBlock(form_classname='subtitle', required=True)), ('cover_image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('image1', wagtail.images.blocks.ImageChooserBlock(required=False)), ('image2', wagtail.images.blocks.ImageChooserBlock(required=False)), ('image3', wagtail.images.blocks.ImageChooserBlock(required=False)), ('image4', wagtail.images.blocks.ImageChooserBlock(required=False)), ('image5', wagtail.images.blocks.ImageChooserBlock(required=False)), ('image6', wagtail.images.blocks.ImageChooserBlock(required=False))])), ('collaborate', wagtail.blocks.StructBlock([('backgroundcolor', wagtail.blocks.CharBlock(form_classname='backgroundcolor', required=False)), ('maintextcolor', wagtail.blocks.CharBlock(form_classname='maintextcolor', required=False)), ('sidetitle', wagtail.blocks.CharBlock(form_classname='sidetitle', required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('title', wagtail.blocks.RichTextBlock(form_classname='title', required=False)), ('button', wagtail.blocks.StreamBlock([('primarybutton', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('icon', wagtail.images.blocks.ImageChooserBlock(required=False)), ('link', wagtail.blocks.PageChooserBlock(can_choose_root=True, required=False))]))], required=False))])), ('ourvalues', wagtail.blocks.StructBlock([('sidetitle', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('title', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('word1', wagtail.blocks.CharBlock(form_classname='word1', required=True)), ('word2', wagtail.blocks.CharBlock(form_classname='word2', required=True)), ('word3', wagtail.blocks.CharBlock(form_classname='word3', required=True)), ('word4', wagtail.blocks.CharBlock(form_classname='word4', required=True)), ('word5', wagtail.blocks.CharBlock(form_classname='word5', required=True))])), ('ourjourney', wagtail.blocks.StructBlock([('sidetitle', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('title', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('subtitle', wagtail.blocks.RichTextBlock(form_classname='subtitle', required=True)), ('ourjourneycards', wagtail.blocks.StreamBlock([('ourjourneycard', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('title', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('subtitle', wagtail.blocks.CharBlock(form_classname='subtitle', required=True)), ('blog_link', wagtail.blocks.PageChooserBlock(can_choose_root=True, required=False))]))]))])), ('ourgallery', wagtail.blocks.StructBlock([('sidetitle', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('title', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('gallery', wagtail.blocks.StreamBlock([('gallery', wagtail.blocks.ListBlock(wagtail.images.blocks.ImageChooserBlock()))]))])), ('ourtestimonial', wagtail.blocks.StructBlock([('sidetitle', wagtail.blocks.CharBlock(form_classname='content', required=True)), ('name', wagtail.blocks.CharBlock(form_classname='content', required=True)), ('designation', wagtail.blocks.CharBlock(form_classname='content', required=True)), ('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('content', wagtail.blocks.RichTextBlock(form_classname='content', required=True)), ('svg', wagtail.images.blocks.ImageChooserBlock(required=False))]))], null=True),
        ),
    ]
