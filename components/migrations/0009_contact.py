# Generated by Django 5.0.3 on 2024-04-09 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('components', '0008_delete_herosection'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]