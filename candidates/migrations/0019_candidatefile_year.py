# Generated by Django 4.1.1 on 2022-10-04 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candidates', '0018_searchquery'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidatefile',
            name='year',
            field=models.CharField(max_length=4, null=True),
        ),
    ]