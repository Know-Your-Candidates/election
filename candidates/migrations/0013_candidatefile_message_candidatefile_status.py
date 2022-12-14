# Generated by Django 4.0 on 2022-09-12 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candidates', '0012_candidatefile'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidatefile',
            name='message',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='candidatefile',
            name='status',
            field=models.CharField(choices=[('Success', 'Success'), ('Failed', 'Failed'), ('Uploading', 'Uploading')], max_length=50, null=True),
        ),
    ]
