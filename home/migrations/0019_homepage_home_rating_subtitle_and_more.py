# Generated by Django 5.0.3 on 2024-04-03 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0018_homepage_great_place_to_work_badge'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='home_rating_subtitle',
            field=models.CharField(blank=True, help_text='Services Navigation Link', max_length=255),
        ),
        migrations.AddField(
            model_name='homepage',
            name='home_rating_title',
            field=models.CharField(blank=True, help_text='Services Navigation Link', max_length=255),
        ),
    ]
