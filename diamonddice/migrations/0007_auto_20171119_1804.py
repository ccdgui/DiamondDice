# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-11-19 18:04
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('diamonddice', '0006_coin'),
    ]

    operations = [
        migrations.RenameField(
            model_name='coin',
            old_name='hand',
            new_name='wallet',
        ),
    ]