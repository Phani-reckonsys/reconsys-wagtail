# Generated by Django 5.0.3 on 2024-04-04 11:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0030_homepage_navbar'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homepage',
            name='navbar',
        ),
    ]
