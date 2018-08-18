from django.urls import include, path
from TwitterClone.twitter_clone_router import TwitterCloneRouter
from TwitterClone.views import *


router = TwitterCloneRouter()
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
