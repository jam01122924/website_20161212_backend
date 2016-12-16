from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Character(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=255, blank=False, unique=True, default='')
    SEX_CHOICE = (('M', 'Male'), ('F', 'Female'))
    sex = models.CharField(max_length=1, choices=SEX_CHOICE, default='M')
    talent = models.ManyToManyField('Talent')
    attributes = models.OneToOneField('Attributes', null=True, on_delete=models.CASCADE)

    owner = models.ForeignKey('auth.User', related_name='character', on_delete=models.CASCADE)

    class Meta:
        ordering = ('created',)


class Attributes(models.Model):
    strength = models.IntegerField(blank=False, default=5)
    perception = models.IntegerField(blank=False, default=5)
    endurance = models.IntegerField(blank=False, default=5)
    charisma = models.IntegerField(blank=False, default=5)
    intelligence = models.IntegerField(blank=False, default=5)
    agility = models.IntegerField(blank=False, default=5)
    luck = models.IntegerField(blank=False, default=5)


class OldJob(models.Model):
    name = models.CharField(max_length=255, default='')
    description = models.TextField(blank=True, null=True)
    attributes = models.OneToOneField('Attributes', null=True, on_delete=models.CASCADE)


class Talent(models.Model):
    id = models.CharField(max_length=255, primary_key=True, db_index=True)
    name = models.CharField(max_length=255, blank=True, default='')
    isPickable = models.BooleanField(blank=True, default=True)
    description = models.TextField(blank=True, null=True)
    effect = models.ManyToManyField('Effect', blank=True)


class Effect(models.Model):
    field = models.CharField(max_length=255, db_index=True)
    value = models.FloatField()
    type = models.CharField(max_length=1, default='')


class Skill(models.Model):
    name = models.CharField(max_length=255, db_index=True)

