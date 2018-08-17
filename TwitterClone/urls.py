from django.urls import include, path
from rest_framework.routers import DefaultRouter
from TwitterClone.views import *


router = DefaultRouter()
router.register('usuarios', PerfilViewSet, base_name='usuarios')
router.register('tweets', TweetViewSet, base_name='tweets')
router.register('comentarios', ComentarioViewSet, base_name='comentarios')

#
# Url Patterns
#

urlpatterns = [
    path('', include(router.urls)),
]
