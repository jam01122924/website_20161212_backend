"""api_102 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token

from character import urls as CharacterUrl
from userInfo import urls as UserInfoUrl

routeLists = (
    CharacterUrl.routeList,
    UserInfoUrl.routeList,
)
router = DefaultRouter()
for routeList in routeLists:
    for route in routeList:
        router.register(route[0], route[1])


urlpatterns = [
    # url(r'^', include('userInfo.urls')),
    url(r'^', include(router.urls)),
    url(r'^api/admin/', admin.site.urls),
    url(r'^api/character/', include('character.urls')),
    url(r'^api/user-info/', include('userInfo.urls')),
    url(r'^api/api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/api-token-auth/', obtain_jwt_token),
]
