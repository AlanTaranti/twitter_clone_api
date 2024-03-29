from rest_framework import serializers
from TwitterClone.models import *
from rest_framework.reverse import reverse


class ComentarioSerializer(serializers.ModelSerializer):
    links = serializers.SerializerMethodField()
    usuario = serializers.SlugRelatedField(slug_field="username", read_only=True)
    tweet = serializers.PrimaryKeyRelatedField(queryset=Tweet.objects.all())

    class Meta:
        model = Comentario
        fields = ("id", "usuario", "texto", "tweet", "links")
        read_only_fields = ("id", "usuario")

    @classmethod
    def setup_eager_loading(cls, queryset):
        # Faz o "carregamento ansioso" dos dados relacionados para evitar a query N+1
        queryset = queryset.select_related("usuario", "tweet")
        return queryset

    def get_links(self, obj):
        request = self.context["request"]
        return {
            "self": reverse(
                "comentarios-detail",
                kwargs={"pk": obj.pk},
                request=request,
            ),
            "usuario": reverse(
                "usuarios-detail",
                kwargs={"pk": obj.usuario.pk},
                request=request,
            ),
            "tweet": reverse(
                "tweets-detail",
                kwargs={"pk": obj.tweet.pk},
                request=request,
            ),
        }
