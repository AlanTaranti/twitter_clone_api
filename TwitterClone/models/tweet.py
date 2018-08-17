from django.db import models
from django.contrib.auth.models import User


class Tweet(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    # O limite do Tweet original é 280. Vamos ser fiéis, :-P
    texto = models.CharField(max_length=280)

    def __str__(self):
        return self.texto
