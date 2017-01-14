from rest_framework import serializers
from character.models import *
from django.contrib.auth.models import User


#
# class UserSerializer(serializers.ModelSerializer):
#     userInfo = UserInfoSerializer(read_only=True)
#     securityQuestion = SecurityQuestionSerializer(many=True)
#
#     class Meta:
#         model = User
#         fields = ('url', 'id', 'username', 'password', 'email', 'is_staff', 'userInfo', 'securityQuestion')
#         write_only_fields = ('password',)
#         read_only_fields = ('is_staff', 'is_superuser', 'is_active', 'date_joined',)
#
#     def create(self, validated_data):
#         # call set_password on user object. Without this
#         # the password will be stored in plain text.
#         print validated_data
#         user = User(username=validated_data['username'],
#                     password=validated_data['password'],
#                     email=validated_data['email'])
#
#         user.set_password(validated_data['password'])
#         user.save()
#
#         for item in validated_data['securityQuestion']:
#             sq = SecurityQuestion(question=item['question'], answer=item['answer'], owner=user)
#             sq.save()
#         return user










class AttributesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attributes
        fields = ('id', 'strength', 'perception', 'endurance', 'charisma', 'intelligence', 'agility', 'luck')


class EffectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Effect
        fields = ('id', 'field', 'value', 'type')


class TalentSerializer(serializers.ModelSerializer):
    effect = EffectSerializer(read_only=True, many=True)
    class Meta:
        model = Talent
        fields = ('id', 'name', 'description', 'effect')


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


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = ('id', 'hp', 'max_hp', 'ap', 'max_ap', 'weight', 'weight_max', 'stamina', 'max_stamina',
                  'skillPoint', 'exp', 'lv', 'dodge_rate', 'hit_rate', 'crt_rate', 'crt_dmg',
                  'hunger', 'thirst', 'health', 'melee_dmg', 'range_dmg', 'energy_dmg', 'persuade_rate',
                  'food_need', 'water_need', 'rest_rate', 'recover_rate', 'fire_resist',
                  'cold_resist', 'energy_resist', 'poison_resist', 'radiation_resist')


class OldJobSerializer(serializers.ModelSerializer):
    attributes = AttributesSerializer(read_only=True)
    talent = TalentSerializer(read_only=True)

    class Meta:
        model = OldJob
        fields = ('id', 'name', 'description', 'talent', 'attributes')


class CharacterSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    oldJob = OldJobSerializer(read_only=True)
    talent = TalentSerializer(read_only=True, many=True)
    skill = SkillSerializer(read_only=True, many=True)
    status = StatusSerializer()
    attributes = AttributesSerializer(read_only=True)

    class Meta:
        model = Character
        fields = ('id', 'created', 'name', 'sex', 'oldJob', 'talent', 'skill', 'status', 'attributes', 'owner')
        read_only_fields = ('owner',)

    # def create(self, validated_data):
    #     print validated_data
    #     character = Character(talent=validated_data['talent'],
    #                         name=validated_data['name'],
    #                         sex=validated_data['sex'],
    #                         skill=validated_data['skill'],
    #                         oldJob=validated_data['oldJob'])
    #     character.save()
    #     # attributes = Attributes(strength=validated_data['attributes'].strength,
    #     #                         perception=validated_data['attributes'].perception,
    #     #                         endurance=validated_data['attributes'].endurance,
    #     #                         charisma=validated_data['attributes'].charisma,
    #     #                         intelligence=validated_data['attributes'].intelligence,
    #     #                         agility=validated_data['attributes'].agility,
    #     #                         luck=validated_data['attributes'].luck)
    #     # print character
    #     # print attributes
    #     # attributes.save()
    #     # character.attributes = attributes
    #     # character.save()
    #     return character


class UserSerializer(serializers.HyperlinkedModelSerializer):
    characters = CharacterSerializer(source='character', many=True, read_only=True)

    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'is_staff', 'characters')


