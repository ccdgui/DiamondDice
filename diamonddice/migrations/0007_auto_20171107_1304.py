# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-11-07 13:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('diamonddice', '0006_dicehand_created_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dice_1',
            fields=[
                ('dicehand_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='diamonddice.Dicehand')),
                ('dice_value', models.IntegerField(default=0)),
                ('dice_status', models.CharField(default='unlocked', max_length=30)),
            ],
            bases=('diamonddice.dicehand',),
        ),
        migrations.CreateModel(
            name='Dice_2',
            fields=[
                ('dicehand_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='diamonddice.Dicehand')),
                ('dice_value', models.IntegerField(default=0)),
                ('dice_status', models.CharField(default='unlocked', max_length=30)),
            ],
            bases=('diamonddice.dicehand',),
        ),
        migrations.CreateModel(
            name='Dice_3',
            fields=[
                ('dicehand_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='diamonddice.Dicehand')),
                ('dice_value', models.IntegerField(default=0)),
                ('dice_status', models.CharField(default='unlocked', max_length=30)),
            ],
            bases=('diamonddice.dicehand',),
        ),
        migrations.CreateModel(
            name='Dice_4',
            fields=[
                ('dicehand_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='diamonddice.Dicehand')),
                ('dice_value', models.IntegerField(default=0)),
                ('dice_status', models.CharField(default='unlocked', max_length=30)),
            ],
            bases=('diamonddice.dicehand',),
        ),
        migrations.CreateModel(
            name='Dice_5',
            fields=[
                ('dicehand_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='diamonddice.Dicehand')),
                ('dice_value', models.IntegerField(default=0)),
                ('dice_status', models.CharField(default='unlocked', max_length=30)),
            ],
            bases=('diamonddice.dicehand',),
        ),
        migrations.RemoveField(
            model_name='dicehand',
            name='dice_status1',
        ),
        migrations.RemoveField(
            model_name='dicehand',
            name='dice_status2',
        ),
        migrations.RemoveField(
            model_name='dicehand',
            name='dice_status3',
        ),
        migrations.RemoveField(
            model_name='dicehand',
            name='dice_status4',
        ),
        migrations.RemoveField(
            model_name='dicehand',
            name='dice_status5',
        ),
        migrations.RemoveField(
            model_name='dicehand',
            name='dice_value1',
        ),
        migrations.RemoveField(
            model_name='dicehand',
            name='dice_value2',
        ),
        migrations.RemoveField(
            model_name='dicehand',
            name='dice_value3',
        ),
        migrations.RemoveField(
            model_name='dicehand',
            name='dice_value4',
        ),
        migrations.RemoveField(
            model_name='dicehand',
            name='dice_value5',
        ),
    ]
