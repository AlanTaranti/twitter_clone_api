from django.db import models
from django.contrib.auth.models import User


class Perfil(models.Model):
    # Relação 1:1 com usuário do Django
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)

    # A simetria falsa é necessário para simular a assimetria do Twitter:
    #   Nem todas as pessoas que você segue, te segue de volta
    segue = models.ManyToManyField('self', symmetrical=False)

    def __str__(self):
        return self.usuario.username
