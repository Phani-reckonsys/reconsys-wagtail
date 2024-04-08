# Generated by Django 5.0.3 on 2024-04-07 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('components', '0003_herosection_herosection_subtitle_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='herosection',
            name='herosection_subtitle',
            field=models.CharField(blank=True, help_text='Services Navigation Link', max_length=500),
        ),
        migrations.AlterField(
            model_name='herosection',
            name='herosection_title',
            field=models.CharField(blank=True, help_text='Services Navigation Link', max_length=500),
        ),
    ]