from django.urls import include, path
from rest_framework.routers import DefaultRouter
from TwitterClone.views import *


router = DefaultRouter()
router.register('usuarios', PerfilViewSet, base_name='usuarios')

#
# Url Patterns
#

urlpatterns = [
    path('', include(router.urls)),
]
