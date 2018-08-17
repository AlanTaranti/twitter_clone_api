from rest_framework import serializers
from TwitterClone.models import *
from rest_framework.reverse import reverse
from django.contrib.auth.models import User


class TweetSerializer(serializers.ModelSerializer):
    links = serializers.SerializerMethodField()
    usuario = serializers.SlugRelatedField(slug_field='username', queryset=User.objects.all())

    class Meta:
        model = Tweet
        fields = ('id', 'usuario', 'texto', 'links')
        read_only_fields = ('id', 'usuario')

    @classmethod
    def setup_eager_loading(cls, queryset):
        # Faz o "carregamento ansioso" dos dados relacionados para evitar a query N+1
        queryset = queryset.select_related('usuario')
        return queryset

    def get_links(self, obj):
        request = self.context['request']
        return {
            'self': reverse('tweets-detail',
                            kwargs={'pk': obj.pk},
                            request=request,
                            ),
            'usuario': reverse('usuarios-detail',
                               kwargs={'pk': obj.usuario.pk},
                               request=request,
                               ),
        }
