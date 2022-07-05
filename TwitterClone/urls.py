from django.urls import include, path
from TwitterClone.twitter_clone_router import TwitterCloneRouter
from TwitterClone.views import *


router = TwitterCloneRouter()
router.register("usuarios", UserViewSet, basename="usuarios")
router.register("tweets", TweetViewSet, basename="tweets")
router.register("comentarios", ComentarioViewSet, basename="comentarios")
router.register("feed", FeedViewSet, basename="feed")

#
# Url Patterns
#

urlpatterns = [
    path("", include(router.urls)),
]
