from rest_framework import serializers
from userInfo.models import UserInfo, SecurityQuestion
from django.contrib.auth.models import User


class SecurityQuestionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SecurityQuestion
        fields = ('id', 'question', 'answer')


class UserInfoSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    securityQuestions = SecurityQuestionSerializer(many=True, read_only=True)

    class Meta:
        model = UserInfo
        fields = ('firstName', 'lastName', 'owner', 'securityQuestions')


class UserSerializer(serializers.ModelSerializer):
    userInfo = UserInfoSerializer(read_only=True)
    securityQuestion = SecurityQuestionSerializer(many=True)

    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'password', 'email', 'is_staff', 'userInfo', 'securityQuestion')
        write_only_fields = ('password',)
        read_only_fields = ('is_staff', 'is_superuser', 'is_active', 'date_joined',)

    def create(self, validated_data):
        # call set_password on user object. Without this
        # the password will be stored in plain text.
        print validated_data
        user = User(username=validated_data['username'],
                    password=validated_data['password'],
                    email=validated_data['email'])

        user.set_password(validated_data['password'])
        user.save()

        for item in validated_data['securityQuestion']:
            sq = SecurityQuestion(question=item['question'], answer=item['answer'], owner=user)
            sq.save()
        return user
