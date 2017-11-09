# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-11-08 19:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('diamonddice', '0008_mydicehand'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dice_value', models.IntegerField(default=0)),
                ('dice_status', models.CharField(default='unlocked', max_length=30)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('dicehand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='diamonddice.Dicehand')),
            ],
        ),
        migrations.RemoveField(
            model_name='dice_1',
            name='dicehand_ptr',
        ),
        migrations.RemoveField(
            model_name='dice_2',
            name='dicehand_ptr',
        ),
        migrations.RemoveField(
            model_name='dice_3',
            name='dicehand_ptr',
        ),
        migrations.RemoveField(
            model_name='dice_4',
            name='dicehand_ptr',
        ),
        migrations.RemoveField(
            model_name='dice_5',
            name='dicehand_ptr',
        ),
        migrations.DeleteModel(
            name='MyDicehand',
        ),
        migrations.DeleteModel(
            name='Dice_1',
        ),
        migrations.DeleteModel(
            name='Dice_2',
        ),
        migrations.DeleteModel(
            name='Dice_3',
        ),
        migrations.DeleteModel(
            name='Dice_4',
        ),
        migrations.DeleteModel(
            name='Dice_5',
        ),
    ]
