from django.urls import include, path
from rest_framework.routers import DefaultRouter
from TwitterClone.views import *


router = DefaultRouter()
router.register('usuarios', UserViewSet, base_name='usuarios')
router.register('tweets', TweetViewSet, base_name='tweets')
router.register('comentarios', ComentarioViewSet, base_name='comentarios')
router.register('feed', FeedViewSet, base_name='feed')

#
# Url Patterns
#

urlpatterns = [
    path('', include(router.urls)),
]
