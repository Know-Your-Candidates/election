# Generated by Django 4.1.1 on 2022-09-19 19:33

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('candidates', '0016_alter_candidatefile_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='candidate_image',
            field=cloudinary.models.CloudinaryField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='candidate',
            name='party_image',
            field=cloudinary.models.CloudinaryField(max_length=255, null=True),
        ),
    ]
