"""podmon URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""

from django.conf.urls import url, include
from rest_framework import routers
from podmon.api.views import UserView, UsersView, RegisterView, AccountView
from podmon.api.views.character_view import character_urls
from django.contrib import admin
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token
from rest_framework_extensions.routers import ExtendedSimpleRouter

base_router = routers.DefaultRouter()
base_router.register(r'user', UserView, base_name='user')
base_router.register(r'users', UsersView, base_name='users')
base_router.register(r'account', AccountView, base_name='account')

urlpatterns = [
    url(r'^', include(base_router.urls)),
    url(r'^account/(?P<account_id>[a-z0-9]+)/character/(?P<char_id>[a-z0-9]+)/', include(character_urls)),
    url(r'^admin/', admin.site.urls),
    url(r'^register/', RegisterView),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^docs/', include('rest_framework_swagger.urls')),
    url(r'^token/fetch', obtain_jwt_token),
    url(r'^token/refresh', refresh_jwt_token),
    url(r'^token/verify', verify_jwt_token)
]
