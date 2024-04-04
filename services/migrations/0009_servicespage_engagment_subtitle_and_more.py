# Generated by Django 5.0.3 on 2024-04-04 17:00

import django.db.models.deletion
import modelcluster.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0008_alter_businesshelpedcardpoint_page'),
        ('wagtailimages', '0025_alter_image_file_alter_rendition_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicespage',
            name='engagment_subtitle',
            field=models.CharField(blank=True, help_text='Business helped subtitle', max_length=255),
        ),
        migrations.AddField(
            model_name='servicespage',
            name='engagment_title',
            field=models.CharField(blank=True, help_text='Business helped subtitle', max_length=255),
        ),
        migrations.CreateModel(
            name='EngagmentCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('title', models.CharField(blank=True, help_text='Services Navigation Link', max_length=255)),
                ('subtitle', models.CharField(blank=True, help_text='Services Navigation Link', max_length=255)),
                ('cover_image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image')),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='engagment_card', to='services.servicespage')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
    ]
