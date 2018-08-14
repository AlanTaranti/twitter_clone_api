from TwitterClone.serializers import PerfilSerializer
from rest_framework import viewsets
from django.contrib.auth.models import User


class PerfilViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = PerfilSerializer
    filter_fields = ('username', 'email')
    search_fields = ('username', 'first_name', 'last_name', 'email')
