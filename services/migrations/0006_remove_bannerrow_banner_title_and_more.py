# Generated by Django 5.0.3 on 2024-04-04 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0005_remove_servicespage_banner_title_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bannerrow',
            name='banner_title',
        ),
        migrations.AddField(
            model_name='servicespage',
            name='banner_title',
            field=models.CharField(blank=True, help_text='Banner section title', max_length=255),
        ),
    ]
