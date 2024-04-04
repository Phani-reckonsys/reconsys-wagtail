# Generated by Django 5.0.3 on 2024-04-04 16:28

import django.db.models.deletion
import modelcluster.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0007_servicespage_businesshelped_subtitle_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='businesshelpedcardpoint',
            name='page',
            field=modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='business_helped_card_point', to='services.businesshelpedcard'),
        ),
    ]
