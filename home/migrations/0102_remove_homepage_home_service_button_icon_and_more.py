# Generated by Django 5.0.3 on 2024-04-23 07:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0101_homepage_outline_grey_button'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homepage',
            name='home_service_button_icon',
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='home_service_button_text',
        ),
    ]
