# Generated by Django 5.0.3 on 2024-04-07 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0037_homepage_home_whyreckonsys_content_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='home_casestudies_subtitle',
            field=models.CharField(blank=True, help_text='Services Navigation Link', max_length=255),
        ),
        migrations.AddField(
            model_name='homepage',
            name='home_casestudies_title',
            field=models.CharField(blank=True, help_text='Services Navigation Link', max_length=255),
        ),
    ]
