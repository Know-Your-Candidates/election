# Generated by Django 4.0 on 2022-09-16 22:14

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('candidates', '0013_candidatefile_message_candidatefile_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidatefile',
            name='file',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='file'),
        ),
    ]
