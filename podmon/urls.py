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
from podmon.api.views import UserView, UsersView, RecipeView, RecipeListView, TagView, RegisterView
from django.contrib import admin

router = routers.DefaultRouter()
router.register(r'user', UserView, base_name='user')
router.register(r'users', UsersView)
router.register(r'recipes', RecipeView)
router.register(r'recipe-list', RecipeListView)
router.register(r'tags', TagView)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^admin/', admin.site.urls),
    url(r'^register/', RegisterView),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^docs/', include('rest_framework_swagger.urls')),
    url(r'^token/fetch', 'rest_framework_jwt.views.obtain_jwt_token'),
    url(r'^token/refresh', 'rest_framework_jwt.views.refresh_jwt_token'),
    url(r'^token/verify', 'rest_framework_jwt.views.verify_jwt_token')
]
