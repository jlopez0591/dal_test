# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-27 20:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pruebas', '0003_auto_20170227_2020'),
    ]

    operations = [
        migrations.AddField(
            model_name='country',
            name='code',
            field=models.CharField(default='', max_length=120),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='country',
            name='country_code',
            field=models.CharField(default='', max_length=10),
            preserve_default=False,
        ),
    ]
