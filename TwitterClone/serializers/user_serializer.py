from rest_framework import serializers
from TwitterClone.models import *
from django.contrib.auth.models import User
from rest_framework.reverse import reverse
from django.contrib.auth.hashers import make_password


class NestedSlugRelatedField(serializers.SlugRelatedField):
    #
    # Esta classe permite que possa ser usada a representação slug com chaves estrangeiras
    #
    # Como usar:
    # No campo slug_field, separe os atributos de chave estrangeira com '__'
    #
    # Exemplo:
    # Para referenciar o 'username' de uma chave estrangeira 'usuario'
    # Utilizamos: slug_field='usuario__username'
    #
    # Observação:
    # Assim como é recomendado pelo Django, procure utilizar atributos com valores únicos, como o nome de usuário
    #

    def to_representation(self, obj):
        from copy import copy

        attr = self.slug_field.split("__")
        objeto = copy(obj)
        resposta = None

        for item in attr:
            resposta = getattr(objeto, item)
            if type(resposta) is not str:
                objeto = resposta

        return resposta


class UserSerializer(serializers.ModelSerializer):
    links = serializers.SerializerMethodField()
    tweets = serializers.SlugRelatedField(slug_field="texto", many=True, read_only=True)
    segue = NestedSlugRelatedField(
        many=True,
        slug_field="usuario__username",
        source="perfil.segue",
        queryset=Perfil.objects.all(),
        required=False
    )

    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "first_name",
            "last_name",
            "email",
            "password",
            "tweets",
            "segue",
            "links",
        )
        read_only_fields = ("id", "tweets")
        extra_kwargs = {"password": {"write_only": True}}

    def get_links(self, obj):
        request = self.context["request"]
        return {
            "self": reverse(
                "usuarios-detail",
                kwargs={"pk": obj.pk},
                request=request,
            ),
        }

    def save(self, **kwargs):
        #
        # Sobrescrita do método save do Model Serializer
        #
        # Necessário para utilizar a relação OneToOne entre
        # User e Perfil

        perfil_data = self.validated_data

        perfil_data["password"] = make_password(perfil_data["password"])

        user_instance = super().save(**kwargs)

        segue_data = perfil_data.pop("segue", [])
        Perfil.objects.update_or_create(usuario=user_instance)
        perfil_instance = Perfil.objects.get(usuario=user_instance)

        for item in segue_data:
            perfil_instance.segue.add(Perfil.objects.get(id=item.id))

        return user_instance
