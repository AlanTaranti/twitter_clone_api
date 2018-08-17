from rest_framework import permissions
from django.contrib.auth.models import User


class EhDonoOuLeituraApenas(permissions.BasePermission):
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
