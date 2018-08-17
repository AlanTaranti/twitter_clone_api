import django_filters
from TwitterClone.serializers import TweetSerializer
from rest_framework import viewsets
from TwitterClone.models import Tweet


class TweetFilter(django_filters.FilterSet):
    usuario = django_filters.CharFilter(lookup_expr='username__exact')

    class Meta:
        model = Tweet
        fields = ('usuario',)


class TweetViewSet(viewsets.ModelViewSet):
    serializer_class = TweetSerializer
    filter_class = TweetFilter
    search_fields = ('texto',)

    def get_queryset(self):
        queryset = Tweet.objects.all()
        # Configurar "carregamento ansioso" (o invés do lazy loading do Django) para evitar selects N+1
        queryset = self.get_serializer_class().setup_eager_loading(queryset)
        return queryset