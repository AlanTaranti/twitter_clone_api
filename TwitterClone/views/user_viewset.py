from TwitterClone.serializers import UserSerializer
from rest_framework import viewsets
from django.contrib.auth.models import User
from TwitterClone.models import Perfil
from rest_framework.decorators import action
from rest_framework.response import Response


class UserViewSet(viewsets.ModelViewSet):
    """
    # Endpoint de Usuário

    Nesse endpoint é possível manipular os usuários

    Note que apenas é possível um usuário editar a si mesmo

    **Métodos e ações possíveis:**

    - **GET**
        - /usuarios
            - Lista todos os usuários
            - Parâmetros:
                - Filtragem:
                    - username: filtra um usuário por nome
                    - email: filtra um usuário por email
                - Busca:
                    - search: busca por nomes, sobrenomes, usernames e email de usuários
        - /usuarios/<id\>
            - Consulta um usuário específico
    - **POST**
        - /usuarios
            - Cria um novo usuário
        - /usuarios/<id\>/seguir
            - Segue um usuário
        - /usuarios/<id\>/desseguir
            - Dessegue um usuário
    -  **PUT/PATCH**
        - /usuarios/<id\>
            - Atualiza um usuário específico
    -  **DELETE**
        - /usuarios/<id\>
            - Deleta um usuário específico
    """
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
