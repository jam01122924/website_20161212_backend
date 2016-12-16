from django.contrib.auth.models import User
from django.db.models import Q
from rest_framework import viewsets, generics
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from userInfo.models import UserInfo, SecurityQuestion
from userInfo.serializers import UserInfoSerializer, SecurityQuestionSerializer, UserSerializer
from userInfo.permissions import OnlyAdminOrReadOnly, OnlyAdminOrOwner


# Create your views here.
class UserInfoViewSet(viewsets.ModelViewSet):
    queryset = UserInfo.objects.all()
    serializer_class = UserInfoSerializer
    permission_classes = (OnlyAdminOrOwner,)

    def list(self, request):
        if request.user.is_anonymous():
            return Response(status=403, data={
                "detail": "Authentication credentials were not provided."
            })
        elif not request.user.is_superuser:
            queryset = UserInfo.objects.filter(Q(owner=request.user))
        else:
            queryset = UserInfo.objects.all()

        serializer = UserInfoSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class SecurityQuestionViewSet(viewsets.ModelViewSet):
    queryset = SecurityQuestion.objects.all()
    serializer_class = SecurityQuestionSerializer
    permission_classes = (OnlyAdminOrOwner,)


class UserViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides 'list' and 'detail' actions
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        # allow non-authenticated user to create via POST:
        return (AllowAny() if self.request.method == 'POST'
            else OnlyAdminOrOwner(),)

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
