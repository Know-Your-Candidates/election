# Generated by Django 4.1.1 on 2023-01-13 19:41

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candidates', '0036_remove_location_candidates__polling_cd4c27_idx_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExcelFileData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_type', models.CharField(choices=[('CandidateData', 'CD'), ('LocationData', 'LD')], default='Candidate Data', max_length=14)),
                ('year', models.CharField(max_length=4, null=True)),
                ('data', models.JSONField(null=True)),
                ('parties', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), blank=True, null=True, size=None)),
                ('read', models.BooleanField(default=False)),
            ],
        ),
    ]
