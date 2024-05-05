# Generated by Django 5.0.4 on 2024-05-04 02:58

import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0141_alter_personalblogpage_blogbody'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personalblogpage',
            name='blogbody',
            field=wagtail.fields.StreamField([('blogbody', wagtail.blocks.StructBlock([('profile_image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('name', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('designation', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('about_the_author', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('twitter_url', wagtail.blocks.URLBlock(form_classname='link', required=False)), ('linkedin_url', wagtail.blocks.URLBlock(form_classname='link', required=False)), ('facebook_url', wagtail.blocks.URLBlock(form_classname='link', required=False)), ('url', wagtail.blocks.URLBlock(form_classname='link', required=True)), ('blog_text', wagtail.blocks.RichTextBlock(features=['h2', 'h3', 'h4', 'p', 'bold', 'hr', 'italic', 'code', 'ol', 'ul', 'link', 'image', 'blockquote'], form_classname='title', required=True))]))], null=True),
        ),
    ]