from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Perfil(models.Model):

    # Relação 1:1 com usuário do Django
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)

    # A simetria falsa é necessário para simular a assimetria do Twitter:
    #   Nem todas as pessoas que você segue, te segue de volta
    segue = models.ManyToManyField('self', related_name='seguido', symmetrical=False, null=True)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Perfil.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()
