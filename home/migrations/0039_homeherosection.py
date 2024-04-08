# Generated by Django 5.0.3 on 2024-04-07 15:25

import django.db.models.deletion
import modelcluster.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('components', '0003_herosection_herosection_subtitle_and_more'),
        ('home', '0038_homepage_home_casestudies_subtitle_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomeHeroSection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('home_herosection', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='components.herosection')),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='home_herosection', to='home.homepage')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
    ]
