# Generated by Django 4.0 on 2022-09-06 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candidates', '0006_alter_candidate_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='federal_constituency_code',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='location',
            name='senatorial_district_code',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='location',
            name='state_constituency_code',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
