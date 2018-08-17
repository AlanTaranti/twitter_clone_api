from rest_framework import permissions
from django.contrib.auth.models import User


class TwitterClonePermission(permissions.BasePermission):
    #
    # Permissão a nível do objeto que permite apenas os donos editarem
    # Outros possuem apenas a permissão de leitura
    #
    # Assume que o objeto possui um atributo usuario ou seja um usuario

    def has_object_permission(self, request, view, obj):
        # Permissões de leitura são permitidas a todas as solicitações
        # então, GET, HEAD e OPTIONS estão liberados
        if request.method in permissions.SAFE_METHODS:
            return True

        # A instancia precisar ser um usuário ou ter um atributo usuário
        if type(obj) is User:
            return obj == request.user
        else:
            return obj.usuario == request.user

    def has_permission(self, request, view):

        # Com exceção de criação de conta

        # Todos os usuarios tem permissão de leitura
        if request.method in permissions.SAFE_METHODS:
            return True

        # Usuários anônimos tem permissão de post nos usuários
        elif str(view).split('.')[2] == 'perfil_viewset' and request.method == 'POST':
            return request.user and not request.user.is_authenticated

        # Para o restante dos endpoints, é necessário autenticação para escrita
        else:
            return request.user and request.user.is_authenticated
