# Generated by Django 5.0.3 on 2024-04-10 07:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('components', '0009_contact'),
        ('wagtailcore', '0091_remove_revision_submitted_for_moderation'),
    ]

    operations = [
        migrations.AddField(
            model_name='navbar',
            name='Contact_page',
            field=models.CharField(blank=True, help_text='contactus Link', max_length=255),
        ),
        migrations.AddField(
            model_name='navbar',
            name='Contact_page_link',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.page'),
        ),
        migrations.AlterField(
            model_name='navitem',
            name='name',
            field=models.CharField(blank=True, help_text='Navigation link', max_length=255),
        ),
    ]
