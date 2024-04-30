# Generated by Django 4.2.11 on 2024-04-30 05:16

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUsModel',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(blank=True, max_length=512)),
                ('email', models.EmailField(blank=True, max_length=512, null=True)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('company', models.CharField(blank=True, max_length=512, null=True)),
                ('service', models.CharField(blank=True, max_length=512, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='NewsLetterModel',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('email', models.EmailField(max_length=512, unique=True)),
            ],
        ),
    ]
