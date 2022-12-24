# Generated by Django 4.1.1 on 2022-12-07 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candidates', '0035_alter_location_lga_and_more'),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name='location',
            name='candidates__polling_cd4c27_idx',
        ),
        migrations.AlterField(
            model_name='candidate',
            name='name',
            field=models.CharField(db_index=True, max_length=250),
        ),
        migrations.AlterField(
            model_name='location',
            name='polling_unit',
            field=models.CharField(db_index=True, max_length=1000),
        ),
        migrations.AlterField(
            model_name='location',
            name='state',
            field=models.CharField(db_index=True, max_length=300),
        ),
        migrations.AlterField(
            model_name='location',
            name='ward',
            field=models.CharField(db_index=True, max_length=1024),
        ),
        migrations.AddIndex(
            model_name='candidate',
            index=models.Index(fields=['name'], name='candidates__name_ed6dc8_idx'),
        ),
        migrations.AddIndex(
            model_name='location',
            index=models.Index(fields=['polling_unit_code', 'lga', 'polling_unit', 'ward', 'state'], name='candidates__polling_cef696_idx'),
        ),
    ]