# Generated by Django 5.0.3 on 2024-04-01 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_create_homepage'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='service_nav',
            field=models.CharField(blank=True, help_text='my name is phani', max_length=255),
        ),
    ]
