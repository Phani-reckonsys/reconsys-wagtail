# Generated by Django 5.0.3 on 2024-04-04 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Navbar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_nav', models.CharField(blank=True, help_text='Services Navigation Link', max_length=255)),
                ('ourworks_nav', models.CharField(blank=True, help_text='OurWorks Navigation Link', max_length=255)),
            ],
        ),
    ]
