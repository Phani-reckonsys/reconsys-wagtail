# Generated by Django 5.0.3 on 2024-04-08 02:30

import django.db.models.deletion
import modelcluster.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0040_homecasestudiescard'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='home_testimonials_subtitle',
            field=models.CharField(blank=True, help_text='Services Navigation Link', max_length=255),
        ),
        migrations.AddField(
            model_name='homepage',
            name='home_testimonials_title',
            field=models.CharField(blank=True, help_text='Services Navigation Link', max_length=255),
        ),
        migrations.CreateModel(
            name='HomeTestimonialCard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('name', models.CharField(blank=True, help_text='Services Navigation Link', max_length=255)),
                ('designation', models.CharField(blank=True, help_text='Services Navigation Link', max_length=255)),
                ('content', models.CharField(blank=True, help_text='Services Navigation Link', max_length=255)),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='testimonial_cards', to='home.homepage')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
    ]