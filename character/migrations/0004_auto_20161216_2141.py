# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-16 21:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('character', '0003_auto_20161216_1840'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='talent',
            name='field',
        ),
        migrations.RemoveField(
            model_name='talent',
            name='type',
        ),
        migrations.RemoveField(
            model_name='talent',
            name='value',
        ),
        migrations.AddField(
            model_name='skill',
            name='description',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AddField(
            model_name='skill',
            name='effect',
            field=models.ManyToManyField(null=True, to='character.Effect'),
        ),
        migrations.AddField(
            model_name='skill',
            name='level',
            field=models.IntegerField(default=1, max_length=5),
        ),
        migrations.AddField(
            model_name='talent',
            name='effect',
            field=models.ManyToManyField(null=True, to='character.Effect'),
        ),
        migrations.AlterField(
            model_name='character',
            name='talent',
            field=models.ManyToManyField(null=True, to='character.Talent'),
        ),
    ]
