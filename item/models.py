from __future__ import unicode_literals

from django.db import models
from character.models import Effect

# Create your models here.
class Material(models.Model):
    name = models.CharField(max_length=255, blank=False, unique=True, default='')
    description = models.CharField(max_length=511, blank=False, default='')
    type = models.CharField(max_length=63, blank=False, default='')
    level = models.IntegerField(blank=False, default=1)
    iconUrl = models.CharField(max_length=127, blank=False, default='')


class MaterialInBag(models.Model):
    material = models.ForeignKey('Material', null=True, on_delete=models.CASCADE)
    amount = models.IntegerField(blank=False, default=0)


class MaterialInStorage(models.Model):
    material = models.ForeignKey('Material', null=True, on_delete=models.CASCADE)
    amount = models.IntegerField(blank=False, default=0)


class Equipment(models.Model):
    name = models.CharField(max_length=255, blank=False, unique=True, default='')
    description = models.CharField(max_length=511, blank=False, default='')
    type = models.CharField(max_length=63, blank=False, default='')
    position = models.CharField(max_length=63, blank=False, default='')
    level = models.IntegerField(blank=False, default=1)
    effect = models.ManyToManyField('Effect')


class EquipmentInBag(models.Model):
    material = models.ForeignKey('Equipment', null=True, on_delete=models.CASCADE)
    amount = models.IntegerField(blank=False, default=0)


class EquipmentInStorage(models.Model):
    material = models.ForeignKey('Equipment', null=True, on_delete=models.CASCADE)
    amount = models.IntegerField(blank=False, default=0)
