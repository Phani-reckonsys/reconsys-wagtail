# Generated by Django 5.0.3 on 2024-04-16 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('components', '0013_remove_footeritems_link_remove_socialitems_link_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='navbar',
            name='bgcolor',
            field=models.CharField(blank=True, help_text='contactus Link', max_length=255),
        ),
    ]
