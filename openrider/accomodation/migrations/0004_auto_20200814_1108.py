# Generated by Django 3.0.8 on 2020-08-14 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accomodation', '0003_auto_20200812_1007'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='accomodation',
            name='coordinates',
        ),
        migrations.AlterField(
            model_name='accomodation',
            name='lat',
            field=models.DecimalField(blank=True, decimal_places=6, max_digits=12, null=True),
        ),
        migrations.AlterField(
            model_name='accomodation',
            name='lon',
            field=models.DecimalField(blank=True, decimal_places=6, max_digits=12, null=True),
        ),
    ]
