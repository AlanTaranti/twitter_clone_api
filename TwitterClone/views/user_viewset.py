from TwitterClone.serializers import UserSerializer
from rest_framework import viewsets
from django.contrib.auth.models import User
from TwitterClone.models import Perfil
from rest_framework.decorators import action
from rest_framework.response import Response


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_fields = ('username', 'email')
    search_fields = ('username', 'first_name', 'last_name', 'email')

    @action(methods=['post'], detail=True)
    def seguir(self, request, pk=None):
        perfil_a_seguir = User.objects.get(pk=pk).perfil
        Perfil.objects.get(usuario=request.user).segue.add(perfil_a_seguir)

        serializer = UserSerializer(data=perfil_a_seguir.usuario)
        serializer.is_valid()

        return Response(serializer.data)

    @action(methods=['post'], detail=True)
    def desseguir(self, request, pk=None):
        perfil_a_desseguir = User.objects.get(pk=pk).perfil
        Perfil.objects.get(usuario=request.user).segue.remove(perfil_a_desseguir)

        serializer = UserSerializer(data=perfil_a_desseguir.usuario)
        serializer.is_valid()

        return Response(serializer.data)
