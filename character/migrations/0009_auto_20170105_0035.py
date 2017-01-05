# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2017-01-05 00:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('character', '0008_auto_20161216_2256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='talent',
            field=models.ManyToManyField(to='character.Talent'),
        ),
        migrations.AlterField(
            model_name='skill',
            name='effect',
            field=models.ManyToManyField(to='character.Effect'),
        ),
        migrations.AlterField(
            model_name='skill',
            name='requiredSkill',
            field=models.ManyToManyField(to='character.Skill'),
        ),
        migrations.AlterField(
            model_name='talent',
            name='effect',
            field=models.ManyToManyField(to='character.Effect'),
        ),
    ]