# Generated by Django 5.0.6 on 2024-07-18 11:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('components', '0030_reviewcards'),
        ('wagtailcore', '0093_uploadedfile'),
    ]

    operations = [
        migrations.AddField(
            model_name='reviewcards',
            name='cardlink',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.page'),
        ),
    ]
