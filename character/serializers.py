from rest_framework import serializers
from character.models import *
from django.contrib.auth.models import User


class CharacterSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Character
        fields = ('id', 'created', 'name', 'sex', 'talent', 'owner')


class AttributesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Attributes
        fields = ('strength', 'perception', 'endurance', 'charisma', 'intelligence', 'agility', 'luck')


class OldJobSerializer(serializers.ModelSerializer):
    attributes = AttributesSerializer(read_only=True)

    class Meta:
        model = OldJob
        fields = ('name', 'description', 'attributes')


class EffectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Effect
        fields = ('id', 'field', 'value')


class TalentSerializer(serializers.HyperlinkedModelSerializer):
    effect = EffectSerializer(many=True, read_only=True)

    class Meta:
        model = Talent
        fields = ('id', 'name', 'description', 'effect')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    characters = CharacterSerializer(source='character', many=True, read_only=True)

    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'is_staff', 'characters')
