# Generated by Django 5.0.3 on 2024-04-17 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0088_homepage_home_process_sidetitle_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='home_industries_sidetitle',
            field=models.CharField(blank=True, help_text='Services Navigation Link', max_length=255),
        ),
        migrations.AddField(
            model_name='homepage',
            name='home_rating_sidetitle',
            field=models.CharField(blank=True, help_text='Services Navigation Link', max_length=255),
        ),
    ]
