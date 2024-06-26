# Generated by Django 5.0.3 on 2024-04-16 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('components', '0012_footeritems_socialitems'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='footeritems',
            name='link',
        ),
        migrations.RemoveField(
            model_name='socialitems',
            name='link',
        ),
        migrations.AddField(
            model_name='footeritems',
            name='url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='socialitems',
            name='url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
