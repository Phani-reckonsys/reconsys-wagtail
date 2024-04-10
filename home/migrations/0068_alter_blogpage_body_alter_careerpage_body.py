# Generated by Django 5.0.3 on 2024-04-10 09:38

import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0067_alter_careerpage_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpage',
            name='body',
            field=wagtail.fields.StreamField([('herosecion', wagtail.blocks.StructBlock([('titles', wagtail.blocks.StreamBlock([('title', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('subtitle', wagtail.blocks.CharBlock(form_classname='subtitle', required=True))]))])), ('include_quick_testimonials', wagtail.blocks.BooleanBlock(required=False)), ('primary_button', wagtail.blocks.StreamBlock([('button', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('icon', wagtail.images.blocks.ImageChooserBlock(required=False)), ('link', wagtail.blocks.PageChooserBlock(can_choose_root=True))]))])), ('image_cover', wagtail.images.blocks.ImageChooserBlock(required=False)), ('image_decor', wagtail.images.blocks.ImageChooserBlock(required=False))])), ('ourmission', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('subtitle', wagtail.blocks.CharBlock(form_classname='subtitle', required=True)), ('cover_image', wagtail.images.blocks.ImageChooserBlock(required=False))])), ('ourvision', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('subtitle', wagtail.blocks.CharBlock(form_classname='subtitle', required=True)), ('cover_image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('image1', wagtail.images.blocks.ImageChooserBlock(required=False)), ('image2', wagtail.images.blocks.ImageChooserBlock(required=False)), ('image3', wagtail.images.blocks.ImageChooserBlock(required=False)), ('image4', wagtail.images.blocks.ImageChooserBlock(required=False)), ('image5', wagtail.images.blocks.ImageChooserBlock(required=False)), ('image6', wagtail.images.blocks.ImageChooserBlock(required=False))])), ('ourvalues', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('word1', wagtail.blocks.CharBlock(form_classname='word1', required=True)), ('word2', wagtail.blocks.CharBlock(form_classname='word2', required=True)), ('word3', wagtail.blocks.CharBlock(form_classname='word3', required=True)), ('word4', wagtail.blocks.CharBlock(form_classname='word4', required=True)), ('word5', wagtail.blocks.CharBlock(form_classname='word5', required=True))])), ('ourjourney', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('subtitle', wagtail.blocks.CharBlock(form_classname='subtitle', required=True)), ('ourjourneycards', wagtail.blocks.StreamBlock([('ourjourneycard', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('title', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('subtitle', wagtail.blocks.CharBlock(form_classname='subtitle', required=True))]))]))])), ('ourgallery', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('gallery', wagtail.blocks.StreamBlock([('gallery', wagtail.blocks.ListBlock(wagtail.images.blocks.ImageChooserBlock()))]))])), ('ourtestimonial', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('content', wagtail.blocks.CharBlock(form_classname='content', required=True)), ('svg', wagtail.images.blocks.ImageChooserBlock(required=False))])), ('blogsherosection', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('subtitle', wagtail.blocks.CharBlock(form_classname='subtitle', required=True)), ('cards', wagtail.blocks.StreamBlock([('blogsherosectioncards', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('title', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('subtitle', wagtail.blocks.CharBlock(form_classname='subtitle', required=True))]))]))]))], null=True),
        ),
        migrations.AlterField(
            model_name='careerpage',
            name='body',
            field=wagtail.fields.StreamField([('herosecion', wagtail.blocks.StructBlock([('titles', wagtail.blocks.StreamBlock([('title', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('subtitle', wagtail.blocks.CharBlock(form_classname='subtitle', required=True))]))])), ('include_quick_testimonials', wagtail.blocks.BooleanBlock(required=False)), ('primary_button', wagtail.blocks.StreamBlock([('button', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('icon', wagtail.images.blocks.ImageChooserBlock(required=False)), ('link', wagtail.blocks.PageChooserBlock(can_choose_root=True))]))])), ('image_cover', wagtail.images.blocks.ImageChooserBlock(required=False)), ('image_decor', wagtail.images.blocks.ImageChooserBlock(required=False))])), ('ourmission', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('subtitle', wagtail.blocks.CharBlock(form_classname='subtitle', required=True)), ('cover_image', wagtail.images.blocks.ImageChooserBlock(required=False))])), ('ourvision', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('subtitle', wagtail.blocks.CharBlock(form_classname='subtitle', required=True)), ('cover_image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('image1', wagtail.images.blocks.ImageChooserBlock(required=False)), ('image2', wagtail.images.blocks.ImageChooserBlock(required=False)), ('image3', wagtail.images.blocks.ImageChooserBlock(required=False)), ('image4', wagtail.images.blocks.ImageChooserBlock(required=False)), ('image5', wagtail.images.blocks.ImageChooserBlock(required=False)), ('image6', wagtail.images.blocks.ImageChooserBlock(required=False))])), ('ourvalues', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('word1', wagtail.blocks.CharBlock(form_classname='word1', required=True)), ('word2', wagtail.blocks.CharBlock(form_classname='word2', required=True)), ('word3', wagtail.blocks.CharBlock(form_classname='word3', required=True)), ('word4', wagtail.blocks.CharBlock(form_classname='word4', required=True)), ('word5', wagtail.blocks.CharBlock(form_classname='word5', required=True))])), ('ourjourney', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('subtitle', wagtail.blocks.CharBlock(form_classname='subtitle', required=True)), ('ourjourneycards', wagtail.blocks.StreamBlock([('ourjourneycard', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('title', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('subtitle', wagtail.blocks.CharBlock(form_classname='subtitle', required=True))]))]))])), ('ourgallery', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('gallery', wagtail.blocks.StreamBlock([('gallery', wagtail.blocks.ListBlock(wagtail.images.blocks.ImageChooserBlock()))]))])), ('ourtestimonial', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('content', wagtail.blocks.CharBlock(form_classname='content', required=True)), ('svg', wagtail.images.blocks.ImageChooserBlock(required=False))])), ('blogsherosection', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('subtitle', wagtail.blocks.CharBlock(form_classname='subtitle', required=True)), ('cards', wagtail.blocks.StreamBlock([('blogsherosectioncards', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('title', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('subtitle', wagtail.blocks.CharBlock(form_classname='subtitle', required=True))]))]))]))], null=True),
        ),
    ]
