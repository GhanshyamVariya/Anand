# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-17 21:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Patient', '0009_auto_20180317_2041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='Birth_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='Mobile',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='Name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
