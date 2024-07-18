# Generated by Django 5.0.6 on 2024-07-15 09:08

import django.db.models.deletion
import modelcluster.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('components', '0028_servicesmegamenu_image'),
        ('wagtailcore', '0093_uploadedfile'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServicesItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('name', models.CharField(blank=True, help_text='Navigation link', max_length=255)),
                ('navbar', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='servicesitems', to='components.footer')),
                ('url', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.page')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
    ]