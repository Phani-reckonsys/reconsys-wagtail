# Generated by Django 5.0.4 on 2024-05-20 06:40

import django.db.models.deletion
import wagtail.blocks
import wagtail.contrib.table_block.blocks
import wagtail.fields
import wagtail.images.blocks
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0162_alter_personalblogpage_blogbody'),
        ('wagtailcore', '0091_remove_revision_submitted_for_moderation'),
    ]

    operations = [
        migrations.CreateModel(
            name='TabledpersonalblogPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('blogheader', wagtail.fields.StreamField([('blogheader', wagtail.blocks.StructBlock([('blogs_url', wagtail.blocks.PageChooserBlock(required=False)), ('page_title', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('headline', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('category_title', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('publish_date', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('cover_image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('tags', wagtail.blocks.StreamBlock([('tags', wagtail.blocks.StructBlock([('text', wagtail.blocks.CharBlock(form_classname='title', required=True))]))]))]))], null=True)),
                ('blogbody', wagtail.fields.StreamField([('blogbody', wagtail.blocks.StructBlock([('profile_image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('name', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('designation', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('about_the_author', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('twitter_url', wagtail.blocks.URLBlock(form_classname='link', required=False)), ('linkedin_url', wagtail.blocks.URLBlock(form_classname='link', required=False)), ('facebook_url', wagtail.blocks.URLBlock(form_classname='link', required=False)), ('url', wagtail.blocks.URLBlock(form_classname='link', required=True)), ('blog_text', wagtail.blocks.StructBlock([('blog_text', wagtail.blocks.RichTextBlock(features=['h2', 'h3', 'h4', 'p', 'bold', 'hr', 'italic', 'code', 'ol', 'ul', 'link', 'image', 'blockquote'], form_classname='title', required=True))], classname='title', features=['h2', 'h3', 'h4', 'p', 'bold', 'hr', 'italic', 'code', 'ol', 'ul', 'link', 'image', 'blockquote'], required=True))]))], null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.AlterField(
            model_name='personalblogpage',
            name='blogbody',
            field=wagtail.fields.StreamField([('blogbody', wagtail.blocks.StructBlock([('profile_image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('name', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('designation', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('about_the_author', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('twitter_url', wagtail.blocks.URLBlock(form_classname='link', required=False)), ('linkedin_url', wagtail.blocks.URLBlock(form_classname='link', required=False)), ('facebook_url', wagtail.blocks.URLBlock(form_classname='link', required=False)), ('url', wagtail.blocks.URLBlock(form_classname='link', required=True)), ('blog_text', wagtail.blocks.StructBlock([('blog_text', wagtail.blocks.RichTextBlock(features=['h2', 'h3', 'h4', 'p', 'bold', 'hr', 'italic', 'code', 'ol', 'ul', 'link', 'image', 'blockquote'], form_classname='title', required=True))], classname='title', features=['h2', 'h3', 'h4', 'p', 'bold', 'hr', 'italic', 'code', 'ol', 'ul', 'link', 'image', 'blockquote'], required=True)), ('table', wagtail.blocks.StructBlock([('table', wagtail.contrib.table_block.blocks.TableBlock(required=False, table_options={'contextMenu': ['row_above', 'row_below', '---------', 'col_left', 'col_right', '---------', 'remove_row', 'remove_col', '---------', 'undo', 'redo', '---------', 'copy', 'cut', '---------', 'alignment']}))], required=False, table_options={'contextMenu': ['row_above', 'row_below', '---------', 'col_left', 'col_right', '---------', 'remove_row', 'remove_col', '---------', 'undo', 'redo', '---------', 'copy', 'cut', '---------', 'alignment']}))]))], null=True),
        ),
    ]