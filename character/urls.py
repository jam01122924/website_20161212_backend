from django.conf.urls import url, include

from character import views
from character.views import *
from rest_framework import renderers, routers
from rest_framework.routers import DefaultRouter

# bind ViewSet classes into a set of detailed views:
character_list = CharacterViewSet.as_view({
    'get': 'list',
    'post': 'create',
})
character_detail = CharacterViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})
#
# attributes_list = AttributesViewSet.as_view({
#     'get': 'list'
# })
# attributes_detail = AttributesViewSet.as_view({
#     'get': 'retrieve'
# })

talent_list = TalentViewSet.as_view({
    'get': 'list',
    'post': 'create',
})
talent_detail = TalentViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

effect_list = EffectViewSet.as_view({
    'get': 'list',
    'post': 'create',
})
effect_detail = EffectViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

user_list = OldJobViewSet.as_view({
    'get': 'list'
})
user_detail = OldJobViewSet.as_view({
    'get': 'retrieve'
})

# create a router and register our viewsets with it
router = DefaultRouter()
router.root_view_name = 'test'
router.register(r'character', views.CharacterViewSet)
router.register(r'attributes', views.AttributesViewSet)
router.register(r'oldjob', views.OldJobViewSet)
router.register(r'talent', views.TalentViewSet)
router.register(r'effect', views.EffectViewSet)
router.register(r'users', views.UserViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]

routeList = (
    (r'character', views.CharacterViewSet),
    (r'attributes', views.AttributesViewSet),
    (r'oldjob', views.OldJobViewSet),
    (r'talent', views.TalentViewSet),
    (r'effect', views.EffectViewSet),
    (r'users', views.UserViewSet),
)
