from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Character(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=255, blank=False, unique=True, default='')
    SEX_CHOICE = (('M', 'Male'), ('F', 'Female'))
    sex = models.CharField(max_length=1, choices=SEX_CHOICE, default='M')
    talent = models.ManyToManyField('Talent')
    skill = models.ManyToManyField('Skill')
    attributes = models.OneToOneField('Attributes', null=True, on_delete=models.CASCADE)
    status = models.OneToOneField('Status', null=True, on_delete=models.CASCADE)
    oldJob = models.ForeignKey('OldJob', null=True, on_delete=models.CASCADE)

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


class Effect(models.Model):
    id = models.CharField(primary_key=True, unique=True, max_length=255, db_index=True)
    field = models.CharField(max_length=255, db_index=True)
    value = models.FloatField(default=0.0)
    type = models.CharField(max_length=10, default='')


class OldJob(models.Model):
    name = models.CharField(max_length=255, default='')
    description = models.TextField(blank=True, null=True)
    attributes = models.OneToOneField('Attributes', null=True, on_delete=models.CASCADE)
    talent = models.ForeignKey('Talent', null=True, on_delete=models.CASCADE)


class Talent(models.Model):
    name = models.CharField(max_length=255, blank=True, default='')
    description = models.TextField(blank=True, null=True, default='')
    effect = models.ManyToManyField('Effect')


class Skill(models.Model):
    name = models.CharField(primary_key=True, unique=True, max_length=255, db_index=True)
    description = models.TextField(blank=True, null=True, default='')
    requiredLv = models.IntegerField(default=1)
    requiredSkill = models.ManyToManyField('Skill')
    effect = models.ManyToManyField('Effect')


class Status(models.Model):
    hp = models.IntegerField(default=0)
    max_hp = models.IntegerField(default=0)
    ap = models.IntegerField(default=0)
    max_ap = models.IntegerField(default=0)
    weight = models.FloatField(default=0.0)
    weight_max = models.FloatField(default=0.0)
    stamina = models.IntegerField(default=0)
    max_stamina = models.IntegerField(default=0)
    skillPoint = models.IntegerField(default=0)
    exp = models.IntegerField(default=0)
    lv = models.IntegerField(default=0)

    dodge_rate = models.FloatField(default=0.0)
    hit_rate = models.FloatField(default=0.0)
    crt_rate = models.FloatField(default=0.0)
    crt_dmg = models.FloatField(default=0.0)

    hunger = models.FloatField(default=0.0)
    thirst = models.FloatField(default=0.0)
    health = models.FloatField(default=0.0)

    melee_dmg = models.FloatField(default=0.0)
    range_dmg = models.FloatField(default=0.0)
    energy_dmg = models.FloatField(default=0.0)

    persuade_rate = models.FloatField(default=0.0)
    food_need = models.FloatField(default=0.0)
    water_need = models.FloatField(default=0.0)
    rest_rate = models.FloatField(default=0.0)
    recover_rate = models.FloatField(default=0.0)

    fire_resist = models.FloatField(default=0.0)
    cold_resist = models.FloatField(default=0.0)
    energy_resist = models.FloatField(default=0.0)
    poison_resist = models.FloatField(default=0.0)
    radiation_resist = models.FloatField(default=0.0)
