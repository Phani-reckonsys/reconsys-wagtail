# Generated by Django 5.0.4 on 2024-05-07 12:08

import wagtail.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0034_remove_servicespage_faqsection_title_bottom_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bannerrow',
            name='banner_text',
            field=wagtail.fields.RichTextField(blank=True, help_text='Services Navigation Link', max_length=450),
        ),
    ]
