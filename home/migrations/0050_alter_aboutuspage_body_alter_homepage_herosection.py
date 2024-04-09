# Generated by Django 5.0.3 on 2024-04-09 12:36

import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0049_alter_aboutuspage_body_alter_homepage_herosection'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutuspage',
            name='body',
            field=wagtail.fields.StreamField([('herosecion', wagtail.blocks.StructBlock([('titles', wagtail.blocks.StreamBlock([('title', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('subtitle', wagtail.blocks.CharBlock(form_classname='subtitle', required=True))]))])), ('primary_button', wagtail.blocks.StreamBlock([('button', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('icon', wagtail.images.blocks.ImageChooserBlock(required=False)), ('link', wagtail.blocks.PageChooserBlock(can_choose_root=True))]))])), ('include_quick_testimonials', wagtail.blocks.BooleanBlock(required=False))]))], null=True),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='herosection',
            field=wagtail.fields.StreamField([('herosecion', wagtail.blocks.StructBlock([('titles', wagtail.blocks.StreamBlock([('title', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('subtitle', wagtail.blocks.CharBlock(form_classname='subtitle', required=True))]))])), ('primary_button', wagtail.blocks.StreamBlock([('button', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('icon', wagtail.images.blocks.ImageChooserBlock(required=False)), ('link', wagtail.blocks.PageChooserBlock(can_choose_root=True))]))])), ('include_quick_testimonials', wagtail.blocks.BooleanBlock(required=False))]))], null=True),
        ),
    ]
