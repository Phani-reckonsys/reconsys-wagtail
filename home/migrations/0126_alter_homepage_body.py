# Generated by Django 5.0.3 on 2024-04-26 13:17

import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0125_alter_contactuspage_body_alter_ourworkspage_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='body',
            field=wagtail.fields.StreamField([('hometesimonials', wagtail.blocks.StructBlock([('sidetitle', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('title', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('subtitle', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('testimonialcards', wagtail.blocks.StreamBlock([('testimonialcard', wagtail.blocks.StructBlock([('review', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('name', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('designation', wagtail.blocks.CharBlock(form_classname='title', required=True))]))])), ('ratingcards', wagtail.blocks.StreamBlock([('ratingcard', wagtail.blocks.StructBlock([('star1', wagtail.images.blocks.ImageChooserBlock(required=False)), ('star2', wagtail.images.blocks.ImageChooserBlock(required=False)), ('star3', wagtail.images.blocks.ImageChooserBlock(required=False)), ('star4', wagtail.images.blocks.ImageChooserBlock(required=False)), ('star5', wagtail.images.blocks.ImageChooserBlock(required=False)), ('url', wagtail.blocks.URLBlock(form_classname='link', required=True)), ('rating', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('review_count', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('logo', wagtail.images.blocks.ImageChooserBlock(required=False))]))]))])), ('homeblogs', wagtail.blocks.StructBlock([('sidetitle', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('title', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('subtitle', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('blogcard', wagtail.blocks.StreamBlock([('blogcard', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('title', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('category', wagtail.blocks.CharBlock(form_classname='category', required=True)), ('info', wagtail.blocks.CharBlock(form_classname='info', required=True)), ('link', wagtail.blocks.URLBlock(form_classname='link', required=True))]))]))])), ('badges', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('badgefield', wagtail.blocks.StreamBlock([('image', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False))]))]))]))], null=True),
        ),
    ]