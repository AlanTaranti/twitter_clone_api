import django_filters
from TwitterClone.serializers import ComentarioSerializer
from rest_framework import viewsets
from TwitterClone.models import Comentario


class ComentarioFilter(django_filters.FilterSet):
    username = django_filters.CharFilter(
        field_name="usuario", lookup_expr="username__exact"
    )

    class Meta:
        model = Comentario
        fields = ("username",)


class ComentarioViewSet(viewsets.ModelViewSet):
    """
    # Endpoint de Comentário

    Nesse endpoint é possível manipular os comentários de um tweet

    Note que apenas é possível um usuário editar seus próprios comentários

    **Métodos e ações possíveis:**

    - **GET**
        - /comentarios
            - Lista todos os comentários
            - Parâmetros:
                - Filtragem:
                    - username: filtra os comentários de um usuário
                - Busca:
                    - search: busca comentários por texto
        - /comentarios/<id\>
            - Consulta um comentários específico
    - **POST**
        - /comentarios
            - Cria um novo comentário
    -  **PUT/PATCH**
        - /comentarios/<id\>
            - Atualiza um comentário específico
    -  **DELETE**
        - /comentarios/<id\>
            - Deleta um comentário específico
    """

    serializer_class = ComentarioSerializer
    filter_class = ComentarioFilter
    search_fields = ("texto",)

    def get_queryset(self):
        queryset = Comentario.objects.all()
        # Configurar "carregamento ansioso" (o invés do lazy loading do Django) para evitar selects N+1
        queryset = self.get_serializer_class().setup_eager_loading(queryset)
        return queryset

    def perform_create(self, serializer):
        serializer.validated_data["usuario"] = self.request.user
        super().perform_create(serializer)
