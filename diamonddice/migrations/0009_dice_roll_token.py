# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-12-01 00:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diamonddice', '0008_coin_coin_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='dice',
            name='roll_token',
            field=models.IntegerField(default=0),
        ),
    ]