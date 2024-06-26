# Generated by Django 5.0.3 on 2024-04-02 09:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_homepage_home_service_subtitle'),
        ('wagtailimages', '0025_alter_image_file_alter_rendition_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='home_service_content',
            field=models.CharField(blank=True, help_text='Services Navigation Link', max_length=255),
        ),
        migrations.CreateModel(
            name='HomeServiceCard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, help_text='Services Navigation Link', max_length=255)),
                ('description', models.CharField(blank=True, help_text='Services Navigation Link', max_length=255)),
                ('card_icon', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image')),
                ('home_page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='service_cards', to='home.homepage')),
            ],
        ),
    ]
