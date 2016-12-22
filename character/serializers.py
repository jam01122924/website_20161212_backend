from rest_framework import serializers
from character.models import *
from django.contrib.auth.models import User


class CharacterSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Character
        fields = ('id', 'created', 'name', 'sex', 'oldJob', 'talent', 'owner')


class AttributesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attributes
        fields = ('strength', 'perception', 'endurance', 'charisma', 'intelligence', 'agility', 'luck')


class EffectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Effect
        fields = ('id', 'field', 'value', 'type')


class TalentSerializer(serializers.ModelSerializer):
    effect = EffectSerializer(read_only=True, many=True)
    class Meta:
        model = Talent
        fields = ('name', 'description', 'effect')


class RequiredSkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ('name', 'description', 'requiredLv')


class SkillSerializer(serializers.ModelSerializer):
    effect = EffectSerializer(read_only=True, many=True)
    requiredSkill = RequiredSkillSerializer(read_only=True, many=True)

    class Meta:
        model = Skill
        fields = ('name', 'description', 'requiredLv', 'requiredSkill', 'effect')


class OldJobSerializer(serializers.ModelSerializer):
    attributes = AttributesSerializer(read_only=True)
    talent = TalentSerializer(read_only=True)

    class Meta:
        model = OldJob
        fields = ('name', 'description', 'talent', 'attributes')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    characters = CharacterSerializer(source='character', many=True, read_only=True)

    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'is_staff', 'characters')
