# Generated by Django 4.1.1 on 2022-12-01 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candidates', '0030_alter_candidatefile_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidatefile',
            name='type',
            field=models.CharField(choices=[('Candidate Data', 'CD'), ('Location Data', 'LD')], default='Candidate Data', max_length=14),
        ),
    ]
