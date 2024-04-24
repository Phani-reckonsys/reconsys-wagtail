# Generated by Django 5.0.3 on 2024-04-24 10:20

import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0028_alter_servicespage_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicespage',
            name='body',
            field=wagtail.fields.StreamField([('herosection', wagtail.blocks.StructBlock([('sidetitles', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('content', wagtail.blocks.StreamBlock([('herocontent', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('subtitle', wagtail.blocks.CharBlock(form_classname='subtitle', required=True)), ('btn_title', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('btn_icon', wagtail.images.blocks.ImageChooserBlock(required=False)), ('btn_link', wagtail.blocks.PageChooserBlock(can_choose_root=True)), ('include_fullimage', wagtail.blocks.BooleanBlock(required=False)), ('image_cover', wagtail.images.blocks.ImageChooserBlock(required=False)), ('image_decor', wagtail.images.blocks.ImageChooserBlock(required=False))]))])), ('include_companies', wagtail.blocks.BooleanBlock(required=False)), ('company_image', wagtail.blocks.StreamBlock([('image', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True))]))]))]))], null=True),
        ),
    ]
