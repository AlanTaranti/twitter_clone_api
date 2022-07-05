from django.db import models
from django.contrib.auth.models import User


class Comentario(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    tweet = models.ForeignKey(
        "Tweet", related_name="comentarios", on_delete=models.CASCADE
    )

    # O limite do comentario original é 280. Vamos ser fiéis, :-P
    texto = models.CharField(max_length=280)

    def __str__(self):
        return "{} - {}: {}".format(self.id, self.usuario.username, self.texto)
