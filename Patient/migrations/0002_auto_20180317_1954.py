# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-17 19:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Patient', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='Date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='Name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]