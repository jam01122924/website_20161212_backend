from __future__ import unicode_literals

from django.db import models


# Create your models here.
class UserInfo(models.Model):
    firstName = models.CharField(max_length=255, default='')
    lastName = models.CharField(max_length=255, default='')

    # owner = models.OneToOneField('auth.User', on_delete=models.CASCADE)


class SecurityQuestion(models.Model):
    question = models.CharField(max_length=255, default='')
    answer = models.CharField(max_length=255, default='')
    owner = models.ForeignKey('auth.User', related_name='securityQuestion', on_delete=models.CASCADE)
