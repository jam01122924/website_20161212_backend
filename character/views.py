from django.contrib.auth.models import User
from django.db.models import Q
from rest_framework import viewsets
from rest_framework.response import Response

from character.models import *
from character.serializers import *
from userInfo.permissions import OnlyAdminOrReadOnly, OnlyAdminOrOwner


# Create your views here.
class CharacterViewSet(viewsets.ModelViewSet):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer
    permission_classes = (OnlyAdminOrOwner,)

    def list(self, request):
        if request.user.is_anonymous():
            return Response(status=403, data={
                "detail": "Authentication credentials were not provided."
            })
        elif not request.user.is_superuser:
            queryset = Character.objects.filter(Q(owner=request.user))
        else:
            queryset = Character.objects.all()

        serializer = CharacterSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data)
    #     content = {
    #         'user': unicode(request.user),  # `django.contrib.auth.User` instance.
    #         'anonymous': unicode(request.user.is_anonymous()),  # `django.contrib.auth.User` instance.
    #         'auth': unicode(request.auth),  # None
    #         'request': unicode(request),  # None
    #     }
    #     return Response(content)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class AttributesViewSet(viewsets.ModelViewSet):
    queryset = Attributes.objects.all()
    serializer_class = AttributesSerializer
    permission_classes = (OnlyAdminOrReadOnly,)


class OldJobViewSet(viewsets.ModelViewSet):
    queryset = OldJob.objects.all()
    serializer_class = OldJobSerializer
    permission_classes = (OnlyAdminOrReadOnly,)


class TalentViewSet(viewsets.ModelViewSet):
    queryset = Talent.objects.all()
    serializer_class = TalentSerializer
    permission_classes = (OnlyAdminOrReadOnly,)


class EffectViewSet(viewsets.ModelViewSet):
    queryset = Effect.objects.all()
    serializer_class = EffectSerializer
    permission_classes = (OnlyAdminOrReadOnly,)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides 'list' and 'detail' actions
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (OnlyAdminOrOwner,)

    def list(self, request):
        if request.user.is_anonymous():
            return Response(status=403, data={
                "detail": "Authentication credentials were not provided."
            })
        elif not request.user.is_superuser:
            queryset = User.objects.filter(Q(id=request.user.id))
        else:
            queryset = User.objects.all()

        serializer = UserSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data)
