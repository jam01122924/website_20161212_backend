from django.conf.urls import url, include

from userInfo import views
from userInfo.views import UserInfoViewSet, SecurityQuestionViewSet, UserViewSet
from rest_framework import renderers
from rest_framework.routers import DefaultRouter

# bind ViewSet classes into a set of detailed views:
userInfo_list = UserInfoViewSet.as_view({
    'get': 'list',
    'post': 'create',
})
userInfo_detail = UserInfoViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

securityQuestion_list = SecurityQuestionViewSet.as_view({
    'get': 'list',
    'post': 'create',
})
securityQuestion_detail = SecurityQuestionViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

user_list = UserViewSet.as_view({
    'get': 'list'
})
user_detail = UserViewSet.as_view({
    'get': 'retrieve'
})

# create a router and register our viewsets with it
router = DefaultRouter()
router.register(r'userInfo', views.UserInfoViewSet)
router.register(r'securityQuestions', views.SecurityQuestionViewSet)
router.register(r'users', views.UserViewSet)

urlpatterns = [
    url(r'^', include(router.urls))
]

routeList = (
    (r'userInfo', views.UserInfoViewSet),
    (r'securityQuestions', views.SecurityQuestionViewSet),
    (r'users', views.UserViewSet),
)
