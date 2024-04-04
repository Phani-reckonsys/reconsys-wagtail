# Generated by Django 5.0.3 on 2024-04-04 17:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0011_remove_engagmentcard_data_engagmentcard_cover_image_and_more'),
        ('wagtailimages', '0025_alter_image_file_alter_rendition_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicespage',
            name='testimonial_avatar',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image'),
        ),
        migrations.AddField(
            model_name='servicespage',
            name='testimonial_content',
            field=models.CharField(blank=True, help_text='Business helped subtitle', max_length=255),
        ),
        migrations.AddField(
            model_name='servicespage',
            name='testimonial_desigation',
            field=models.CharField(blank=True, help_text='Business helped subtitle', max_length=255),
        ),
        migrations.AddField(
            model_name='servicespage',
            name='testimonial_name',
            field=models.CharField(blank=True, help_text='Business helped subtitle', max_length=255),
        ),
    ]
