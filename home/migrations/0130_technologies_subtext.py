# Generated by Django 5.0.3 on 2024-04-28 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0129_technologies_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='technologies',
            name='subtext',
            field=models.CharField(blank=True, help_text='Technology Stack Group Name', max_length=255),
        ),
    ]
