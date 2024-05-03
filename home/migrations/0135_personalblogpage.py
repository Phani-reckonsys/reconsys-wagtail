# Generated by Django 5.0.4 on 2024-05-03 16:06

import django.db.models.deletion
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0134_alter_careerpage_body_alter_contactuspage_body_and_more'),
        ('wagtailcore', '0091_remove_revision_submitted_for_moderation'),
    ]

    operations = [
        migrations.CreateModel(
            name='PersonalblogPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('blogheader', wagtail.fields.StreamField([('blogheader', wagtail.blocks.StructBlock([('page_title', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('headline', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('category_title', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('publish_date', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('decorimage', wagtail.images.blocks.ImageChooserBlock(required=False)), ('tags', wagtail.blocks.StreamBlock([('tags', wagtail.blocks.StructBlock([('text', wagtail.blocks.CharBlock(form_classname='title', required=True))]))]))]))], null=True)),
                ('blogbody', wagtail.fields.StreamField([('blogbody', wagtail.blocks.StructBlock([('page_title', wagtail.blocks.RichTextBlock(form_classname='title', required=True))]))], null=True)),
                ('blogAuthor', wagtail.fields.StreamField([('blogauthor', wagtail.blocks.StructBlock([('profile_image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('name', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('designation', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('abouttheauthor', wagtail.blocks.CharBlock(form_classname='title', required=True))]))], null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]