# Generated by Django 5.0.3 on 2024-04-05 05:29

import django.db.models.deletion
import modelcluster.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0032_button'),
    ]

    operations = [
        migrations.AlterField(
            model_name='button',
            name='button',
            field=modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='button', to='home.homepage', unique=True),
        ),
    ]
