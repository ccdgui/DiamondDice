# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-11-05 21:21
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('diamonddice', '0005_dicehand_display_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='dicehand',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2017, 11, 5, 21, 21, 41, 358046, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
