# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-16 22:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('character', '0012_auto_20170116_2254'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='oldjob',
            name='talent',
        ),
        migrations.AddField(
            model_name='oldjob',
            name='talent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='character.Talent'),
        ),
    ]
