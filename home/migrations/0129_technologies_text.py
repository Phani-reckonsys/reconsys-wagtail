# Generated by Django 5.0.3 on 2024-04-28 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0128_alter_homepage_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='technologies',
            name='text',
            field=models.CharField(blank=True, help_text='Technology Stack Group Name', max_length=255),
        ),
    ]
