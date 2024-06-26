# Generated by Django 5.0.3 on 2024-04-09 05:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('components', '0005_footer'),
        ('wagtailcore', '0091_remove_revision_submitted_for_moderation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='navbar',
            name='ourworks_nav',
        ),
        migrations.RemoveField(
            model_name='navbar',
            name='service_nav',
        ),
        migrations.CreateModel(
            name='NavItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('name', models.CharField(blank=True, help_text='Services Navigation Link', max_length=255)),
                ('link', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.page')),
                ('navbar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='navitems', to='components.navbar')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
    ]
