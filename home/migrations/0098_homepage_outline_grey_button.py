# Generated by Django 5.0.3 on 2024-04-23 05:43

import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0097_alter_homepage_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='outline_grey_button',
            field=wagtail.fields.StreamField([('button', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('icon', wagtail.images.blocks.ImageChooserBlock(required=False)), ('link', wagtail.blocks.PageChooserBlock(can_choose_root=True))]))], default=2),
            preserve_default=False,
        ),
    ]
