# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-11-15 21:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diamonddice', '0003_auto_20171113_1836'),
    ]

    operations = [
        migrations.AddField(
            model_name='dice',
            name='alldice_locked',
            field=models.CharField(default='No', max_length=3),
        ),
    ]
