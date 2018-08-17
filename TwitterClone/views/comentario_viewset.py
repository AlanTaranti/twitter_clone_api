import django_filters
from TwitterClone.serializers import ComentarioSerializer
from rest_framework import viewsets
from TwitterClone.models import Comentario


class ComentarioFilter(django_filters.FilterSet):
    usuario = django_filters.CharFilter(lookup_expr='username__exact')

    class Meta:
        model = Comentario
        fields = ('usuario',)


class ComentarioViewSet(viewsets.ModelViewSet):
    serializer_class = ComentarioSerializer
    filter_class = ComentarioFilter
    search_fields = ('texto',)

    def get_queryset(self):
        queryset = Comentario.objects.all()
        # Configurar "carregamento ansioso" (o invés do lazy loading do Django) para evitar selects N+1
        queryset = self.get_serializer_class().setup_eager_loading(queryset)
        return queryset
