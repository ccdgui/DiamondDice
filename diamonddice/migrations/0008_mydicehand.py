# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-11-07 16:00
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('diamonddice', '0007_auto_20171107_1304'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyDicehand',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('diamonddice.dicehand',),
        ),
    ]
