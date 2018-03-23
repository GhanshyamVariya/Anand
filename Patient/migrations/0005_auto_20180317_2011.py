# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-17 20:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Patient', '0004_patient_treatment_desciption'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='Blood_Pressure',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='Pulse',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='SPO2',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='Temperature',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
